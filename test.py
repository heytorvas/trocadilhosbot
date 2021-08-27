import requests, yaml

import sqlite3
#from sqlite3 import Error

import requests
with open('env.yaml', 'r') as f:
    TOKEN = yaml.safe_load(f)['TOKEN']
# response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates').json()
# print(response)

################## TA FUNCIONANDO ##################
response = requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=491934003&text=Testando arroba!')
print(response)













# for i in response['result']:
#     user = i['message']['from']

#con = sqlite3.connect('database.db')
# for i in response['result']:
#     user = i['message']['from']
    
#     cursor = con.cursor()
#     cursor.execute("INSERT OR IGNORE INTO user(id,is_bot,first_name,last_name,username,language_code) VALUES (?,?,?,?,?,?);", 
#             (user['id'], user['is_bot'], 
#             user['first_name'], user['last_name'], 
#             user['username'], user['language_code']))
#     con.commit()
    # cursor.close()

# cursor = con.cursor()
# cursor.execute("SELECT * FROM user;")
# cursor.close()
# print(cursor.fetchall())





# def create_table(conn, create_table_sql):
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object
#     :param create_table_sql: a CREATE TABLE statement
#     :return:
#     """
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)

# sql_create_user_table = """CREATE TABLE IF NOT EXISTS user (
#                                 id integer PRIMARY KEY,
#                                 is_bot integer NOT NULL,
#                                 first_name text NOT NULL,
#                                 last_name text NOT NULL,
#                                 username text NOT NULL,
#                                 language_code text NOT NULL
#                             );"""

# database = 'database.db'

# conn = create_connection(database)

# # create tables
# if conn is not None:
#     # create tasks table
#     create_table(conn, sql_create_user_table)
# else:
#     print("Error! cannot create the database connection.")


