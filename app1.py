from flask import Flask, make_response, request
import subprocess

app = Flask(__name__)


@app.route('/')
def home():
    response = make_response("Welcome to app1")
    response.headers['CustomHeader'] = 'TestHeader'
    return response


@app.route('/error')
def error():
    return 1 / 0


@app.route('/ping')
def ping():
    host = request.args.get('host', '127.0.0.1')

    result = subprocess.run(
        f"ping -c 1 {host}",
        shell=True,
        capture_output=True,
        text=True
    )

    return result.stdout


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
