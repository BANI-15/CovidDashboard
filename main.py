from flask import Flask
server = Flask(__name__)

@server.route('/')
def home_page():
    return 'Home Page!'

@server.route('/data')
def data_page():
    return 'Data page !'


server.run(host='0.0.0.0', debug=True)