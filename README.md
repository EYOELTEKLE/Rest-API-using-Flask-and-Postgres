# Rest API with Flask, Postgres, psycopg2
## Usage
	

 - Install postgres from https://www.postgresql.org/
 - Make sure you have installed python
 - create a local python Environment
 - install the requirements packages using **pip install -r requirements.txt**
 - Create .env file to setup your DB credentials
 - set up host, database, db_name, db_password
 - initialize the DB by using **python init_db.py**
 - run the flask rest API using **python app.py**
 - Play with the endpoints
	- "/" for get 
	-  "/api/users" for get too
	-  "/api/users/id" for get , to get  a single user
	-  ""/api/users" for post, with necessary users body fields(name & job)
	-  "/api/users/id " for delete with necessary user body fields(name & job)
	-  "/api/users/id " for put with necessary user body fields(name & job)
	# Requirements
- click==8.1.3
- colorama==0.4.6
- Flask==2.2.3
- importlib-metadata==6.6.0
- itsdangerous==2.1.2
- Jinja2==3.1.2
- MarkupSafe==2.1.2
- psycopg2-binary==2.9.6
- python-dotenv==1.0.0
- Werkzeug==2.2.3
- zipp==3.15.0
## table structure
- fields - [id, name, job]
## Author
- Eyoel Tekle ❤️
