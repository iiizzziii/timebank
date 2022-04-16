from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlalchemy

app = Flask(__name__)
db = SQLAlchemy()
# meno = root / heslo = timebank
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:timebank@127.0.0.1:3306/timebank")
connection = engine.connect() # optional???
SQLALCHEMY_DATABASE_URI = "mariadb+mariadbconnector://root:timebank@127.0.0.1:3306/timebank"
SQLALCHEMY_TRACK_MODIFICATIONS = False

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, index=True, unique=True)
    phone = db.Column(db.String(13), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)

class Service(Base):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(300), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship('User', order_by='User.id', backref='service')

class Deal(Base):
    __tablename__ = 'deals'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    service_id = db.Column(db.Integer, db.ForeignKey("services.id"), nullable=False)
    consumer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # service_id.user_id != consumer_id
    date = db.Column(db.Date)
    hours = db.Column(db.Integer)
    done = db.Column(db.Boolean, default=False)

    service = db.relationship('Service', order_by='Service.id', backref='deals')
    consumer = db.relationship('User', order_by='User.id', backref='deals')

# "HANDLE_DB"
# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

# Session = sqlalchemy.orm.sessionmaker()
# Session.configure(bind=engine)
# Session = Session()

# PRIDAVANIE DAT DO DB ***AK NECHCETE PRIDAVAT PO RIADKOCH ZMENTE PREMENNU "add2db" 
# add2db = User(name='lacike',phone='+421999999999',password='heslo1')
# add2db = User(name='ferko',phone='+421777777777',password='heslo2')
# add2db = Service(description='pepe',user_id=1)
# add2db = Deal(service_id=1,consumer_id=2,date=datetime.now(),hours=1)

# Session.add(add2db)
# Session.commit()

@app.route('/')
def index():
    return 'sicko bavi'

app.run(debug=True)