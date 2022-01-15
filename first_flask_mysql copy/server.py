from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend
app = Flask(__name__)

#Add this new route to retrieve data from database and display on browser
@app.route('/')
def index():
    # calling the get_all method from the friends.py
    friends = Friend.get_all()
    print(friends)
    # passing all friends to our template so we can display them there
    return render_template("index.html", all_friends = friends)

@app.route('/friend/show/<int:id>')
def show(id):
    # calling the get_one method and supplying it with the id of the friend we want to get
    friend = Friend.get_one(id)
    return render_template("show_friend.html, friend=friend")

@app.route('/create_friend', methods=["POST"])
def create_friend():
    # Since request.form is a dictionary with the names of our inputs we can use it as our data dictionary that we
    #pass to our save method. (Note: Make sure the names on your form inputs match their corresponding placeholders in        the query)
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ": request.form["occ"]
    }
    # We pass the form data into the save method from the Friend class.
    Friend.save(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/friend/update/<int:id>', methods = ['POST'])
def update():
    Friend.update(request.form, id)
    return redirect('/users')

@app.route('/friend/delete/<int:id>')
def delete(id):
    Friend.delete(id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)