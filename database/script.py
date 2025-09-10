# Do not include 

import sqlite3

def execute_sql_file(database_path, sql_file_path):

   
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        
        with open(sql_file_path, 'r') as sql_file:
            sql_script = sql_file.read()
        
        cursor.executescript(sql_script)
        conn.commit()
        print("Database created ")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()


DATABASE_PATH = 'data.db'
SQL_FILE_PATH = 'schema.sql'

execute_sql_file(DATABASE_PATH, SQL_FILE_PATH)