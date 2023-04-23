import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

localhost = os.getenv("host")
flask_db = os.getenv("database")
DB_USERNAME = os.getenv("db_name")
DB_PASSWORD = os.getenv("db_password")


conn = psycopg2.connect(
            host=localhost,
                database=flask_db,
                    user=DB_USERNAME,
                        password=DB_PASSWORD,
                        )

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("DROP TABLE IF EXISTS users;")
cur.execute(
            "CREATE TABLE users (id serial PRIMARY KEY,"
                "name varchar (150) NOT NULL,"
                    "job varchar (50) NOT NULL);"
                                )

# Insert data into the table

cur.execute(
            "INSERT INTO users (name, job)" "VALUES (%s, %s)",
                ("ey", "engineer"),
                )


cur.execute(
                    "INSERT INTO users (name, job)" "VALUES (%s, %s)",
                                    ("te", "doctor"),
                                                    )
cur.execute(
                    "INSERT INTO users (name, job)" "VALUES (%s, %s)",
                                    ("mi", "archae"),
                                                    )

conn.commit()

cur.close()
conn.close()

