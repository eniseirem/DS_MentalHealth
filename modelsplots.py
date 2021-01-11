#%% Plot for heatmap of confusion_matrix
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
def heatmap_cm(clf,X, y, acc, name):
    plot_confusion_matrix(clf, X, y)
    plt.title('{0} Accuracy Score: {1}'.format(name,acc), size = 15)
    print("check")
    plt.show()