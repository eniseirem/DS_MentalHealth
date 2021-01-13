import preprocess as pre
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix as cm
import matplotlib.pyplot as plt


data = pre.df #this is the fixed dataset
df3 = pre.df3

y=data["MHC_exist"]
X=data.drop(columns=["MHC_exist", "SurveyID"])
#year of the survey is not relevant here

from sklearn.preprocessing import OneHotEncoder

# Create the encoder to make them easier to work with
encoder = OneHotEncoder(handle_unknown="ignore")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

encoder.fit(X_train)
X_train = encoder.transform(X_train)
X_test = encoder.transform(X_test)

#%% LogisticRegression
lr = LogisticRegression(random_state=42, class_weight=None, solver='lbfgs', max_iter=600)
def LR(X_train, y_train,X_test,y_test):
    lr.fit(X_train, y_train)
    predictions = lr.predict(X_test)
    score = round(accuracy_score(y_test, predictions), 3)
    return score,predictions

score, predictions = LR(X_train, y_train,X_test,y_test)

import modelsplots as mp
mp.heatmap_cm(lr, X_test, y_test, score, "Logistic Regression")


#%%

y=df3["MHC_exist"]
X=df3.drop(columns=["MHC_exist","MHC"])
encoder = OneHotEncoder(handle_unknown="ignore")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
encoder.fit(X_train)
X_train = encoder.transform(X_train)
X_test = encoder.transform(X_test)

score, pre = LR(X_train, y_train,X_test, y_test)
mp.heatmap_cm(lr, X_test, y_test, score, "Logistic Regression")
