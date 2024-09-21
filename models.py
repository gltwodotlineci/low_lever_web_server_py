import psycopg2
from psycopg2.extras import DictCursor
import os
from dotenv import load_dotenv

load_dotenv()


def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('PGADMIN_DEFAULT_PASSWORD'),
            host=os.getenv('HOST'),
            port="5432"
        )
        print(f"Successfully connected to {os.getenv('POSTGRES_DB')}")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    

def select_all_from_table(conn, table_name):
    cur = conn.cursor(cursor_factory=DictCursor)
    query = f"SELECT * FROM {table_name}"
    cur.execute(query)
    result = cur.fetchall()
    return result

def final():
    conn = connect_to_db()
    if conn:
        # Select all rows from a table
        table_name = 'your_table_name'  # Replace with the name of your table
        rows = select_all_from_table(conn, table_name)
        print("Selected rows:")
        for row in rows:
            print(row)

    
final()
