from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/Home/<name>')
def hello_world(name):
    return 'Hello, Welcome to {}'.format(name)

@app.route('/about/<name>')
def about(name):
    return 'Welcome to the {about} page {name}'.format(name=name, about="grand")

@app.route('/profile')
def profile():
    return 'This is the profile page'

if __name__ == '__main__':
    app.run(debug=True)