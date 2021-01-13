import preprocess as pre
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix as cm

data = pre.df #this is the fixed dataset
df2 = pre.df2
df3 = pre.df3
precisions = []
recalls = []
accs = []
print(data.tail)
y=data["MHC_exist"]
X=data.drop(columns=["MHC_exist","MHC"])

from sklearn.preprocessing import OneHotEncoder

# Create the encoder to make them easier to work with
encoder = OneHotEncoder(handle_unknown="ignore")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

encoder.fit(X_train)
X_train = encoder.transform(X_train)
X_test = encoder.transform(X_test)
rf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)

def RF(X_train, y_train,X_test, y_test):
    rf.fit(X_train, y_train)
    predictions = rf.predict(X_test)
    score = round(accuracy_score(y_test, predictions), 3)
    return score, predictions

print(encoder.categories_) # get categories

import modelsplots as mp
score, pre = RF(X_train, y_train,X_test, y_test)

#mp.heatmap_cm(rf, X_test, y_test, score, "Random Forest")


#%% Get numerical feature importances
feature_list = list(data.columns)

importances = list(rf.feature_importances_)
# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
# Print out the feature and importances
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances]

#%%
#What I do not understand is that the model seems like couldn't make the connection between
#MHC and MHC_exist

y=df3["MHC_exist"]
X=df3.drop(columns=["MHC_exist","MHC"])
encoder = OneHotEncoder(handle_unknown="ignore")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
encoder.fit(X_train)
X_train = encoder.transform(X_train)
X_test = encoder.transform(X_test)

score, pre = RF(X_train, y_train,X_test, y_test)
print(encoder.categories_) # get categories
mp.heatmap_cm(rf, X_test, y_test, score, "Random Forest")

#This can be mean that race or gender does not have that much impact when predicting mental health condition.


y=df2["MHC_exist"]
X=df2.drop(columns=["MHC_exist","MHC"])
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

X_train = X_train.apply(lambda col: le.fit_transform(col.astype(str)), axis=0, result_type='expand')
X_test = X_test.apply(lambda col: le.fit_transform(col.astype(str)), axis=0, result_type='expand')

score, pre = RF(X_train, y_train,X_test, y_test)



#print(encoder.categories_) # get categories
#mp.heatmap_cm(rf, X_test, y_test, score, "Random Forest")

