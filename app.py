from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlalchemy

app = Flask(__name__)
db = SQLAlchemy()
# meno = root / heslo = timebank
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:timebank@127.0.0.1:3306/timebank")
SQLALCHEMY_DATABASE_URI = "mariadb+mariadbconnector://root:timebank@127.0.0.1:3306/timebank"
SQLALCHEMY_TRACK_MODIFICATIONS = True

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    password = db.Column(db.String(30), nullable=False)

class Service(Base):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship('User', order_by='User.id', backref='service')

class Deal(Base):
    __tablename__ = 'deals'
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey("services.id"), nullable=False)
    consumer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    date = db.Column(db.Date)
    hours = db.Column(db.Integer)
    done = db.Column(db.Boolean)

    service = db.relationship('Service', order_by='Service.id', backref='deals')
    consumer = db.relationship('User', order_by='User.id', backref='deals')

# "HANDLE_DB"
# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
Session = Session()

# PRIDAVANIE DAT DO DB ***AK NECHCETE PRIDAVAT PO RIADKOCH ZMENTE PREMENNU "add2db" 
# add2db = User(id=1,name='lacike',phone='+421999999999',password='heslo1')
# add2db = User(id=2,name='ferko',phone='+421777777777',password='heslo2')
# add2db = Service(id=1,description='pepe',user_id=1)
# add2db = Deal(id=1,service_id=1,consumer_id=2,date=datetime.now(),hours=1,done=False)

# Session.add(add2db)
# Session.commit()

@app.route('/')
def index():
    return 'sicko bavi'

app.run(debug=True)