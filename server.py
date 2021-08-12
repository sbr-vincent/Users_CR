from flask import Flask, render_template, request, redirect
from users import User
# import the class from users..py
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

# relevant code snippet from server.py

@app.route("/users")
def all_users():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route("/users/<int:num>")
def one_user(num):
    # call the get all classmethod to get all users
    user = User.get_one(num)
    print(user)
    return render_template("readOne.html", one_user = user)

@app.route("/users/<int:num>/edit")
def edit_user(num):
    # call the get all classmethod to get all users
    user = User.get_one(num)
    print(user)
    return render_template("edit.html", one_user = user)

@app.route("/users/<int:num>/update", methods=["POST"])
def update_user(num):
    # call the get all classmethod to get all users
    user = User.get_one(num)
    print(user)
    data = {
        "id": num,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.update(data)
    
    return redirect(f"/users/{num}")

@app.route("/users/new")
def display_form():

    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    new_user_id = User.get_id(data)
    print(new_user_id)
    # Don't forget to redirect after saving to the database.
    return redirect(f"/users/{new_user_id}")

@app.route('/delete_user/<int:num>')
def delete_user(num):
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "id": num,  
    }
    # We pass the data dictionary into the save method from the User class.
    User.delete(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

            
if __name__ == "__main__":
    app.run(debug=True)