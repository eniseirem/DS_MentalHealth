import preprocess as pre
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix as cm
import matplotlib.pyplot as plt


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

lr =LogisticRegression(random_state=42, class_weight=None, solver='lbfgs', max_iter=600)
lr.fit(X_train, y_train)

predictions = lr.predict(X_test)

score = round(accuracy_score(y_test, predictions), 3)
cm1 = cm(y_test, predictions)
from sklearn.metrics import plot_confusion_matrix

plot_confusion_matrix(lr, X_test, y_test)
plt.title('LogisticRegression Accuracy Score: {0}'.format(score), size = 15)
plt.show()

#%% some sauce