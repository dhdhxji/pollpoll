#!/usr/bin/python3

import pymysql

db_host = "127.0.0.1"
db_user = "root"
db_pass = "563555"

db_name = "POLL"
poll_table_name = "Polls"
poll_answ_table_name = "Choises"

poll_table_create_query = """
CREATE TABLE {poll_table_name} (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) NOT NULL)
""".format(**locals())

poll_choise_create_query = """
CREATE TABLE {poll_answ_table_name} (
id INT AUTO_INCREMENT PRIMARY KEY,
poll_id INT NOT NULL,
answer VARCHAR(255) NOT NULL,
percent INT DEFAULT 0,

FOREIGN KEY(poll_id) REFERENCES {poll_table_name}(id))
""".format(**locals())

connection_instanse = pymysql.connect(host=db_host, user=db_user, password=db_pass,
                                    charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
try:
    cursor = connection_instanse.cursor()
    
    cursor.execute("SHOW DATABASES")
    if db_name not in [a['Database'] for a in cursor.fetchall()]:
        cursor.execute("CREATE DATABASE {}".format(db_name))

    cursor.execute("USE {}".format(db_name))

    cursor.execute("SHOW TABLES")
    tables_col_title = "Tables_in_{db_name}".format( **locals() )

    tables = [ a[tables_col_title] for a in cursor.fetchall() ]

    if poll_table_name not in tables:
        cursor.execute(poll_table_create_query)

    if poll_answ_table_name not in tables:
        cursor.execute(poll_choise_create_query)

    print("OK")
except Exception as e:
    print("Exeception occured:{}".format(e))
    connection_instanse.rollback()
finally:
    connection_instanse.close()




