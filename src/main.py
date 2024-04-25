from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def hello_world():
    return 'Hello, Welcome to the flask project!!'

if __name__ == '__main__':
    app.run(debug=True)