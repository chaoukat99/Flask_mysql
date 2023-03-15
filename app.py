# Importing Flask and it  features
from flask import Flask,render_template,request
from flask_mysqldb import MySQL
# initialise the app
app=Flask(__name__)

# connecting with mysql database
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="flask"
mysql=MySQL(app)
@app.route("/",methods=['GET','POST'])
def index():
    if request.method=="POST":
        username=request.form['user']
        password=request.form["pass"]
        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO users(username,pass) VALUES(%s,%s)",(username,password))
        mysql.connection.commit()
        cursor.close()
        return "Success"
       
    return render_template('login.html')
@app.route('/users')
def users():
    cursor=mysql.connection.cursor()
    users=cursor.execute("SELECT * FROM users")
    if users:
        userDetails=cursor.fetchall()
        return render_template('users.html',user_details=userDetails)

if(__name__ == "__main__"):
    app.run(debug=True)    