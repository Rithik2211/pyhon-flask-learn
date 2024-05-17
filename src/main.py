from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def hello_world():
    return 'Hello, Welcome!'

@app.route('/about/<name>')
def about(name):
    array = ["apple","mango","orange","cherry"]
    return render_template("about.html", user_name = name,  data = array, isloggedIn = True)

@app.route('/profile')
def profile():
    return 'This is the profile page'

if __name__ == '__main__':
    app.run(debug=True)