import pandas as pd
import sqlite3
db_file = "data/mental_health.sqlite"
conn = sqlite3.connect(db_file, isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
db_df = pd.read_sql("SELECT * FROM sqlite_master where type = 'table' ", conn)

#db_df = pd.read_sql("SELECT * FROM Answer  ", conn)
db_df = pd.read_sql("SELECT * FROM Answer LEFT JOIN Question ON Answer.QuestionID = Question.questionid", conn)
db_df.to_csv('database.csv', index=False)

db_question = pd.read_sql("SELECT * FROM Question", conn)

#There is to many questions I'll be work on them to decrease the number. However, we do not need to
#work on all of them, we only need the questions which are related to our research.


#Determining the Personal Info Questions
db_question = pd.read_sql("SELECT * FROM Question desc limit 25", conn)
#print(db_question)

#First 3 question has age, gender and country data. We can turn them into columns to have a better understanding

missing_values = ["n/a", "-1","na", "--", " ?","?","nan",-1,"I prefer not to answer"]
data = pd.read_csv("database.csv",  na_values=missing_values) #I'll work with panda csv
#print(data.head())

#data = data.fillna("nan")
import numpy as np
condition = []

condition.append(data["questionid"]==1) #age
data["age"] = np.where(condition[-1], data["AnswerText"], None)
#print(data.head())
data['age'] = data.groupby('UserID')['age'].transform('first')
# filter = (data["questionid"]==1)
# d = (data.where(~filter, inplace = False))
data = data.sort_values('UserID')
#print(data.iloc[:30, -5:])
#we can see the age is showing in the new column. Let's do this with gender and country too.

condition.append(data["questionid"]==2) #gender
data["gender"] = np.where(condition[-1], data[  "AnswerText"], None)
data['gender'] = data.groupby('UserID')['gender'].bfill().ffill()

condition.append(data["questionid"]==3) #country
data["country"] = np.where(condition[-1], data["AnswerText"], None)
data['country'] = data.groupby('UserID')['country'].bfill().ffill()

condition.append(data["questionid"]==89) #gender
data["race"] = np.where(condition[-1], data["AnswerText"], None)
data['race'] = data.groupby('UserID')['race'].bfill().ffill()
#print(data.iloc[:40, -4:])

#print(data["country"].unique)

#let's combine United States and United States of America
data.country = data.country.apply(lambda x: 'USA' if 'United States' in x else x)

print(data["country"].unique())
#we have -1 which is == no-info



print(list(data))
#As seen we have doubled the questionid column probably caused by the merge.
data = data.drop(columns=["QuestionID"])

#let's see our questions
print(list(data))
print(data["questiontext"].nunique()) #we have 105 questions... This will be pain to examine them one by one but what can we do...
#we will drop the gender, country, age questions.
print(data["questiontext"].unique())
print(data["questionid"].nunique())
#'What country do you work in?'

#'Are you self-employed?'
# 'What is your race?  'What is your gender?'  'What country do you live in?'
#  'Overall, how well do you think the tech industry supports employees with mental health issues?'
#  'Overall, how much importance did your previous employer place on mental health?'
#  'Overall, how much importance does your employer place on mental health?'
#  'If yes, what condition(s) have you been diagnosed with?'
# 'If yes, what condition(s) have you been diagnosed with?'
#  'Are you openly identified at work as a person with a mental health issue?'
#  'Have you had a mental health disorder in the past?'
# 'Do you feel that being identified as a person with a mental health issue would hurt your career?'
#    'Has being identified as a person with a mental health issue affected your career?']
#  'If you have revealed a mental health issue to a coworker or employee, do you believe this has impacted you negatively?'
#'Do you currently have a mental health disorder?'
#'If maybe, what condition(s) do you believe you have?'
#  'How easy is it for you to take medical leave for a mental health condition?'


#little check on what we have
found = data[data['questiontext'].str.contains('race')]
print(found[['questionid','questiontext']])
print(found[['questionid','AnswerText']])

#lets drop the gender, country, race columns since we add them as seperate columns.

for condt in condition:
    data = data.drop(data[condt].index)

################################################################################################

#let's see our data

import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

#%% Race
target = data["race"].values #lets see distribution
counter = Counter(target)
perr=[]
for k,v in counter.items():
    per = v / len(target) * 100
    perr.append(per)
    print('Race=%s, Count=%d, Percentage=%.3f%%' % (k, v, per))


#%%
#df_agg = df.groupby(by=["race", "country"]).size().reset_index(name="counts")
# education_perc = sns.countplot(x='race', data=data)
# plt.show()
#
# fig = plt.figure(figsize=(10, 7))
# plt.pie(r, labels=r["race"])
# plt.show()
# sns.barplot(x='race', y='race', data=data, estimator=lambda x: len(x) / len(data) * 100)
# plt.show()

explode = (0, 0.6, 0.5, 0.4, 0.3, 0.2,0,0.0,0.3)
wp = {'linewidth': 1, 'edgecolor': "black"}
print(data.groupby("race"))
data.groupby("race").size().plot(kind='pie', fontsize=10, explode=explode,
                                 wedgeprops=wp,
                                 startangle=90,
                                 )
plt.axis('equal')
plt.ylabel('')
plt.legend(labels=data.groupby("race").groups.keys(), loc="lower left")
plt.tight_layout()
plt.show()
