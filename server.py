from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index(): pass

@app.route('/dev')
def dev(): pass

## I find sollution creating class for routes

class Routes:
    with app.test_request_context():
        index = url_for('index')
        dev = url_for('dev')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)