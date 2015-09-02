from flask import Flask
app = Flask(__name__)


@app.route('/shiyanlou')
def show_hello():
    return 'Hello Jiang Yiying'

if __name__ == '__main__':
   app.run(debug=True)
