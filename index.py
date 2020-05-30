from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print('76544')
    print('LXLG')
    return 'Anakin Skywalker'

@app.route('/hello')
def hello():
    name = "Muga"
    return f'Hello, {name}?'


