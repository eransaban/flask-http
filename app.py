# flask_web/app.py

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
        return '<html><head><title>OpsSchool Mid Project</title></head><body style="background-color:#33E9FF"><p style="text-align: center;font-size:100px"><span style="color:#FFFFFF"><br><br><br>OpsSchool Rulez ;) </span></p></body></html>'


@app.route('/goaway')
def goaway():
    return 'GO AWAY!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
