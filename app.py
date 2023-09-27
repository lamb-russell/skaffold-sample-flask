from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'  # change this text to see if skaffold automatically updates the app

if __name__ == '__main__':
    app.run(host='0.0.0.0')
