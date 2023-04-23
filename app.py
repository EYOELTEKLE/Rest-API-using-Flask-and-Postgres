from flask import Flask, request,  json
from markupsafe import escape
from flask import render_template
import psycopg2
import os
from flask import abort, redirect, url_for
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

localhost = os.getenv("host")
flask_db = os.getenv("database")
DB_USERNAME = os.getenv("db_name")
DB_PASSWORD = os.getenv("db_password")
fake_data = [
    {"name":"ey","id":1,"job":"en"},{"name":"te","id":2,"job":"do"},{"name":"mi","id":3,"job":"ar"}
]

def get_db_connection():
    conn = psycopg2.connect(host=localhost,
            database=flask_db,
            user=DB_USERNAME,
            password=DB_PASSWORD)
    return conn

@app.route("/")
def index():
    return redirect(url_for("get_users"))
@app.route("/api/users")
def get_users():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users;')
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users;
@app.route("/api/users/<int:user_id>")
def get_user(user_id):
     conn = get_db_connection()
     cur = conn.cursor()
     cur.execute("SELECT * FROM users WHERE id = (%s)",(str(user_id)),)
     data = cur.fetchall()
     cur.close()
     conn.close()
     return data

@app.route("/api/users", methods = ['POST'])
def register():
    data = json.loads(request.data)
    if "name" not in data or "job" not in data:
        return "missing data"
    name = data['name']
    job = data['job']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO USERS (name, job)'
                'VALUES (%s,%s)',
                (name, job))
    conn.commit()
    cur.close()
    conn.close()
    return "request submitted great";
@app.route("/api/users/<int:user_id>", methods = ['delete'])
def delete(user_id):
     conn = get_db_connection()
     cur = conn.cursor()
     cur.execute('DELETE FROM users WHERE id = (%s)',(str(user_id)),)
     conn.commit()
     cur.close()
     conn.close()
     return "success"
@app.route("/api/users/<int:user_id>", methods = ['put'])
def update(user_id):
     data = json.loads(request.data)
     if "name" not in data or "job" not in data:
         return "missing data"
     name = data['name']
     job = data['job']
     sql = """ UPDATE users
                SET name = %s, job = %s
                WHERE id = %s"""
     conn = get_db_connection()
     cur = conn.cursor()
     cur.execute(sql, (name,job,str(user_id)))
     conn.commit()
     cur.close()
     conn.close()
     return "success";
@app.errorhandler(404)
def page_not_found(error):
        return render_template('page_not_found.html'), 404
