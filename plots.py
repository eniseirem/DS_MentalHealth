import preprocess as pre
import matplotlib.pyplot as plt

data = pre.data
#%%
# Gender Distribution Pie Chart

explode = (0, 0, 0, 0.3, 0.5)

wp = {'linewidth': 1, 'edgecolor': "black"}
print(data.groupby("gender"))
data.groupby("gender").size().plot(kind='pie', fontsize=10, explode=explode,
                                 wedgeprops=wp,
                                 startangle=90,
autopct='%1.0f%%',
                                   pctdistance=1.1, labeldistance=1.2
                                 )
plt.axis('equal')
plt.ylabel('')
plt.legend(labels=data.groupby("gender").groups.keys(), loc="lower left")
plt.tight_layout()
plt.show()
#%%
# Race Distribution Pie Chart
#

explode = (0, 0.6, 0.5, 0.4, 0.3, 0.2,0,0.0,0.3)
wp = {'linewidth': 1, 'edgecolor': "black"}
#print(data.groupby("race"))
data.groupby("race").size().plot(kind='pie', fontsize=10, explode=explode,
                                 wedgeprops=wp,
                                 startangle=90,
                                 )
plt.axis('equal')
plt.ylabel('')
plt.legend(labels=data.groupby("race").groups.keys(), loc="lower left")
plt.tight_layout()
plt.show()

#%%
# Country Distribution Pie Chart

wp = {'linewidth': 1, 'edgecolor': "black"}
#print(data.groupby("country"))
data.groupby("country").size().plot(kind='pie', fontsize=10,
                                 wedgeprops=wp,
                                 startangle=90,
                                 )
plt.axis('equal')
plt.ylabel('')
plt.legend(labels=data.groupby("country").groups.keys(), loc="lower left")
plt.tight_layout()
#plt.show()