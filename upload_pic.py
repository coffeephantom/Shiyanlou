import os
from flask import Flask, request, render_template
from werkzeug import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = '/Users/coffeephantom/Documents/DevL/Shiyanlou/shiyanlou_cs29/static/uploads'
ALLOWED_EXTENTIONS = set(['jpg', 'JPG', 'jpeg', 'png', 'PNG', 'gif', "GIF"])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DEBUG'] = True


def allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENTIONS


@app.route('/upload_pic', methods=['GET', 'POST'])
def upload_pic():
    if request.method == 'POST':
        # pdb.set_trace()
        f = request.files['the_file']
        if f and allowed_files(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # img_url = url_for('static', filename='uploads/'+filename)
    return render_template('upload_pic.html')


if __name__ == '__main__':
    app.run()
