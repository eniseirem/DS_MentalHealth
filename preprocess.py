import pandas as pd
import sqlite3
db_file = "data/mental_health.sqlite"
conn = sqlite3.connect(db_file, isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
db_df = pd.read_sql("SELECT * FROM sqlite_master where type = 'table' ", conn)
#db_df.to_csv('database.csv', index=False)

#db_df = pd.read_sql("SELECT * FROM Answer  ", conn)
db_df = pd.read_sql("SELECT * FROM Answer LEFT JOIN Question ON Answer.QuestionID = Question.questionid", conn)
db_df.to_csv('database.csv', index=False)

