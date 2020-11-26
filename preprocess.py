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

data = pd.read_csv("database.csv") #I'll work with panda csv
#print(data.head())

import numpy as np

condition = (data["questionid"]==1)
data["age"] = np.where(condition, data["AnswerText"], None)
#print(data.head())
data['age'] = data.groupby('UserID')['age'].transform('first')
# filter = (data["questionid"]==1)
# d = (data.where(~filter, inplace = False))
data = data.sort_values('UserID')
#print(data.iloc[:30, -5:])
#we can see the age is showing in the new column. Let's do this with gender and country too.
condition = (data["questionid"]==2) #gender
data["gender"] = np.where(condition, data["AnswerText"], None)
data['gender'] = data.groupby('UserID')['gender'].bfill().ffill()

condition = (data["questionid"]==3) #country
data["country"] = np.where(condition, data["AnswerText"], None)
data['country'] = data.groupby('UserID')['country'].bfill().ffill()

#print(data.iloc[:40, -4:])

#print(data["country"].unique)

#let's combine United States and United States of America
data.country = data.country.apply(lambda x: 'USA' if 'United States' in x else x)
#TODO: -1 and Ireland check
print(data["country"].unique())
