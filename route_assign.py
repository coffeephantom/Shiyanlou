from flask import Flask, request
app = Flask(__name__)

@app.route('/sum/<int:a>/<int:b>')
def show_sum(a,b):
    return a+b

if __name__ == '__main__':
    app.run()
