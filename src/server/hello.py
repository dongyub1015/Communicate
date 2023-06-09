from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api')
def get_api():
    return {'hello': 'world'}

if __name__ == '__main__':
    app.run(host='0.0.0.0')