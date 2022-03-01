from flask import Flask, request, redirect, session, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "uhiwguiohohiuqfhoiuoyvfebhuowvboyutrbhuofvqjnioqefjniogveohnibeouyrty8dfhbuvdsjknldsjnkzbjhdbgwoqiouaiogvpbehkohnjkn"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable = False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username

@app.route("/")
def main():
    username = request.form["username"]
    user = User.query.filter_by(username=username).first()
    if session["username"] != user.username:
        return render_template("login.html")
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        confirm_password = request.form["confirm-password"]

        if password != confirm_password:
            return render_template("register.html", message="Passwords do not match")

        user = User.query.filter_by(username=username).first()

        if user: 
            return render_template("register.html", message="Username already exists!")    

        user = User(username = username, password=password)

        db.session.add(user)
        db.session.commit()

        session["username"] = user.username

        return redirect("/")
    
    else:
        return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and (user.password == password):
            session["username"] = user.username
            return render_template("index.html", message = "Welcome")
        
        else:
            return render_template("login.html", message = "Invalid username and/or password")
    else:
        return render_template("login.html")
    

@app.route("/logout")
def logout():  
    session.pop("username", None)
    return render_template("login.html")

if __name__ == "__main__":
    db.create_all()
    app.run(host="localhost", port="6284")
