from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlalchemy

app = Flask(__name__)
db = SQLAlchemy()

DB_HOST = "127.0.0.1"
# DB_HOST = "timebank.c6fpgwhpaeto.eu-central-1.rds.amazonaws.com" # AWS
DB_PORT = "3306"
DB_NAME = "timebank"
DB_USERNAME = "root"
DB_PASSWORD = "timebank"  

engine = sqlalchemy.create_engine(f"mariadb+mariadbconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
connection = engine.connect()
SQLALCHEMY_DATABASE_URI = f"mariadb+mariadbconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, index=True, unique=True)
    phone = db.Column(db.String(13), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)

class Job(Base):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(300), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship('User', order_by='User.id', backref='job')

class Deal(Base):
    __tablename__ = 'deals'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_id = db.Column(db.Integer, db.ForeignKey("jobs.id"), nullable=False)
    consumer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # consumer_id != job_id.user_id
    date = db.Column(db.Date)
    hours = db.Column(db.Integer)
    done = db.Column(db.Boolean, default=False)

    job = db.relationship('Job', order_by='Job.id', backref='deals')
    consumer = db.relationship('User', order_by='User.id', backref='deals')

# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

# Session = sqlalchemy.orm.sessionmaker()
# Session.configure(bind=engine)
# Session = Session()

# add2db = User(name='lacike',phone='+421999999999',password='heslo1')
# add2db = User(name='ferko',phone='+421777777777',password='heslo2')
# add2db = Job(description='pepe',user_id=1)
# add2db = Deal(job_id=1,consumer_id=2,date=datetime.now(),hours=1)

# Session.add(add2db)
# Session.commit()

@app.route('/')
def index():
    return 'sicko bavi'

app.run(debug=True)