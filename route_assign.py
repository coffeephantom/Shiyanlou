from flask import Flask, request, flash
app = Flask(__name__)

@app.route('/sum/<int:a>/<int:b>/')
def show_sum(a,b):
    Num = a+b
    return  '%d' %Num

if __name__ == '__main__':
    app.run(debug=True)
