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
#%% some sauce
# from mlxtend.feature_selection import SequentialFeatureSelector as SFS
# from sklearn.pipeline import Pipeline
# import time
# def sfs_(m):
#     global precision
#     global recall
#     global sfs1
#     sfs1 = SFS(lr,
#                    k_features=m,
#                    forward=True,
#                    floating=False,
#                    scoring='accuracy',
#                    n_jobs=-1)
#     # now we can work with our selected features
#     #.fit(X_train.iloc[:, feat_cols], y_train)
#     print("m = " + "{:f}".format(m))
#     pipe = Pipeline([('sfs1', sfs1),
#                               ('LR', lr)])
#     start = time.time()
#     pipe.fit(X_train, y_train)
#     stop = time.time()
#     print(f"Training time: {stop - start}s")
#     print(sfs1.k_feature_idx_)
#     start = time.time()
#     cc = pipe.predict(X_test)
#     acc = pipe.score(X_test, y_test)
#     stop = time.time()
#     print(f"Valid time: {stop - start}s")
#     print(acc)
#     col = pipe.named_steps['sfs1'].k_feature_names_
#     return col, acc
# best_acc = 0
# for m in range(1,9):
#     col, acc = sfs_(m)
#     if acc > best_acc:
#         best_acc = acc
#
# print("Our best accuracy = " + "{:f}".format(best_acc))




#%%
