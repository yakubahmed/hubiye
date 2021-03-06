import os

from flask import Flask, session, render_template, request, redirect, url_for, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
import json



app = Flask(__name__)

# Check for environment variable
#if not os.getenv("DATABASE_URL"):
    #raise RuntimeError("DATABASE_URL is not set")

# onfigure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
Session(app)
# Set up database
engine = create_engine('postgres://ecscjmaijmcnqj:ed862132500d08d40921acc54abb57c148370e89d6ec9d89ff2beed7136bbddd@ec2-54-165-36-134.compute-1.amazonaws.com:5432/d5jspseqo3dpsu')
db = scoped_session(sessionmaker(bind=engine))

def addCity():
    cityname = request.form.get('cityname')
    if db.execute('SELECT * FROM tbl_city WHERE city_name =:cname',{"cname":cityname}).fetchall():
        flash('This city is already found try another one')
        return redirect(url_for('add_manage_city'))
    else:
        res = db.execute("INSERT INTO tbl_city (city_name) VALUES (:cname)", {"cname":cityname})
        db.commit()
        flash('Successfully added')
        return redirect(url_for('add_manage_city'))


    
        
