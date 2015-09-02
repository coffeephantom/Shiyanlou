from flask import Flask,render_template
app = Flask(__name__)

@app.route('/template/')
def hello():
    return render_template('hello_shiyanlou.html')

if name='__main__':
    app.run()

