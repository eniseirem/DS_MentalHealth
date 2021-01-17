import preprocess as pre
import matplotlib.pyplot as plt

data = pre.data
# #%%
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

# wp = {'linewidth': 1, 'edgecolor': "black"}
# #print(data.groupby("country"))
# data.groupby("country").size().plot(kind='pie', fontsize=10,
#                                  wedgeprops=wp,
#                                  startangle=90,
#                                  )
# plt.axis('equal')
# plt.ylabel('')
# plt.legend(labels=data.groupby("country").groups.keys(), loc="lower left")
# plt.tight_layout()
# plt.show() #too mixed

#%%
# Mental Health Condition Distribution Pie Chart
wp = {'linewidth': 1, 'edgecolor': "black"}

data.groupby("MHC_exist").size().plot(kind='pie', fontsize=10,
                                 wedgeprops=wp,
                                 autopct='%1.0f%%',
                                 pctdistance=1.1,
                                 labeldistance=1.2,
                                 startangle=90,
                                 )
plt.axis('equal')
plt.ylabel('')
plt.legend(labels=data.groupby("MHC_exist").groups.keys(), loc="lower left")
plt.tight_layout()
plt.show()

explode = (0, 0, 0, 0.5, 0.4, 0.3,0,0,0.2,0.3,0)
data.groupby("MHC").size().plot(kind='pie', fontsize=10,
                                explode=explode,
                                 wedgeprops=wp,
                                 pctdistance=1.1,
                                 startangle=90,
                                autopct='%1.0f%%',
                                labels=None
                                 )
plt.axis('equal')
plt.ylabel('')

plt.legend(labels=data.groupby("MHC").groups.keys(), bbox_to_anchor=(1,0.5), loc="center right", fontsize=8,
           bbox_transform=plt.gcf().transFigure)
plt.subplots_adjust(left=0.0, bottom=0.1, right=0.7)
plt.tight_layout()
plt.show()

#%%

#%%
# Gender Distribution Pie Chart
#

explode = (0, 0, 0.3, 0.2, 0.1)
wp = {'linewidth': 1, 'edgecolor': "black"}
#print(data.groupby("race"))
data.groupby("gender").size().plot(kind='pie', fontsize=10, explode=explode,
                                 wedgeprops=wp,
                                 startangle=90,
                                 )
plt.axis('equal')
plt.ylabel('')
plt.legend(labels=data.groupby("gender").groups.keys(), loc="lower left")
plt.tight_layout()
plt.show()

#%% by year
import pandas as pd
pd.crosstab(data["MHC_exist"],data.SurveyID).plot(kind='bar')
plt.title('Year by Mental Health')
plt.xlabel('Mental Health')
plt.ylabel('Year')
plt.show()

