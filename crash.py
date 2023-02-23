# LIBRARIES

import time
import requests
import json
import pandas as pd
import warnings
warnings.filterwarnings('ignore') 

############################################################################################################

# FUNCTION TO GET 'N' READ CRASH RESULTS FROM API 
# SET INDEX 
# REC 'N' READ .XLSX

def crash():

  url = requests.get('https://blaze.com/api/crash_games/recent')
  result = json.loads(url.content)
  df = pd.DataFrame(result)
  df = df.set_index('crash_point')
 # print(df)
  df.to_excel('DB1.xlsx')

  time.sleep(300)

  url = requests.get('https://blaze.com/api/crash_games/recent')
  result = json.loads(url.content)
  df = pd.DataFrame(result) 
  df = df.set_index('crash_point')
 # print(df)
  df.to_excel('DB2.xlsx')

  time.sleep(300)

  url = requests.get('https://blaze.com/api/crash_games/recent')
  result = json.loads(url.content)
  df = pd.DataFrame(result)
  df = df.set_index('crash_point')
 # print(df)
  df.to_excel('DB3.xlsx')

############################################################################################################

# FUNCTION TO READ 'N' CONCAT ALL TABLES
def tables():
    table_DB1 = pd.read_excel('DB1.xlsx')
    table_DB2 = pd.read_excel('DB2.xlsx')
    table_DB3 = pd.read_excel('DB3.xlsx')
    table_DBs = pd.concat([table_DB1, table_DB2, table_DB3], ignore_index = True)
    table_DBs.to_excel('DBAll.xlsx')
    table_DBs = pd.read_excel('DBAll.xlsx', parse_dates=['crash_point'], index_col='crash_point')
   
    print(table_DBs)
         

##############################################################################################################

crash()
tables()





