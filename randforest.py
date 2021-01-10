import preprocess as pre
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix as cm
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = pre.df #this is the fixed dataset

y=data["MHC_exist"]
X=data.drop(columns=["MHC_exist"])
from sklearn.preprocessing import OneHotEncoder

# Create the encoder to make them easier to work with
encoder = OneHotEncoder(handle_unknown="ignore")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

encoder.fit(X_train)
X_train = encoder.transform(X_train)
X_test = encoder.transform(X_test)
rf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
rf.fit(X_train, y_train)

predictions = rf.predict(X_test)
score = round(accuracy_score(y_test, predictions), 3)
print(encoder.categories_) # get categories
from sklearn.metrics import plot_confusion_matrix

plot_confusion_matrix(rf, X_test, y_test)
plt.title('RandomForest Accuracy Score: {0}'.format(score), size = 15)
plt.show()
