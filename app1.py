from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def home():
    response = make_response("Welcome to app1")
    response.headers['CustomHeader'] = 'TestHeader'
    return response

@app.route('/error')
def error():
    return 1 / 0

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
