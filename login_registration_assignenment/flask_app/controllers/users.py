from flask import flash, request, render_template, session, redirect

from flask_app import app

from flask_app.models.user import User

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register_user', methods=["POST"])
def register_user():

    if User.validation(request.form) == False:
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form["password"])

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }

    id = User.save_user(data) #save user by id
    session["user_id"] = id #check user if id in session, more secure

    return redirect('/success')

@app.route('/login_user', methods=["POST"])
def login_user():

    user = User.get_by_email(request.form)

    if user == False:
        flash("Not Valid Email", "login_user")
        return redirect('/')
    if bcrypt.check_password_hash(user.password, request.form["password"]) == False:
        flash("Not Valid Password", "login_user")
        return redirect('/')
    session["user_id"] = user.id
    return redirect('/success')

@app.route('/success')
def success():
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "id": session["user_id"]
    }
    return render_template("success.html", user=User.get_by_id(data))

@app.route('/logout_user')
def logout_user():
    session.clear()
    return redirect('/')
