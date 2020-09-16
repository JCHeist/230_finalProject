
# import bottle and sql communications library
from bottle import default_app, route, template, post
import mysql.connector

'''#set up sql connection
conn = mysql.connector.connect(user = 'jcheist', password = 'spencerspencer', host = 'jcheist.mysql.pythonanywhere-services.com', database = 'jcheist$project')

#establich cursor object as c
c = conn.cursor()'''

@route('/')
def hello_world():
    return template("dashboard.html")

@route('/dashboard.html')
def menudash():
    return template("dashboard.html")

@post('/dashboard.html')
def coindash():
    return template("dashboard.html")

@route('/history.html')
def menuhist():
    return template("history.html")

@route('/append.html')
def menuapp():
    return template("append.html")

@post('/confirmappend.html')
def add_verify():
    return template("confirmappend.html")

@route('/delete.html')
def delete():
    return template("delete.html")

@post('/confirmdelete.html')
def delcon():
    return template("confirmdelete.html")

@post('/deleteresult.html')
def delres():
    return template("deleteresult.html")



application = default_app()

