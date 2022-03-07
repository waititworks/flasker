from flask import Flask, render_template

#create flask instance.....
app = Flask(__name__)

#create a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"

# these are filters
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags

def index():
    first_name = "Connor"
    #stuff = "This is <strong>Bold</strong> Text."
    stuff = "this is bold text."
    favortite_pizza = ["Pepperoni","Cheese","Supreme", 41]
    return render_template("index.html",
        first_name=first_name,
        stuff=stuff,
        favortite_pizza=favortite_pizza)

#localhost:5000/user/Connor
@app.route('/user/<name>')
# def user(name):
#     return "<h1>Hello {}!!!</h1>".format(name)
def user(name):
    return render_template("user.html", user_name=name)

# #create custom error page
#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500