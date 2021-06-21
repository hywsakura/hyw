from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world1'

app.run(host='127.0.0.1', port=81)