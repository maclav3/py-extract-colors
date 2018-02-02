import os
import tempfile

from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

from color_extractor import image

app = Flask(__name__)
uploadDir = tempfile.mkdtemp('py-extract-colors-webserver')
app.config['UPLOAD_FOLDER'] = uploadDir


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/histogram', methods=['POST'])
def histogram():
    if not request.method == 'POST':
        return

    f = request.files['file']
    partitions = int(request.form['partitions'])
    nbins = int(request.form['nbins'])

    filename = secure_filename(f.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    f.save(filepath)

    im = image.Image(filepath)
    colors = im.histogram(partitions, nbins)

    return render_template(
        'index.html',
        image=filename,
        filename=f.filename,
        colors=colors,
        max_width=image._resample_size[0],
        max_height=image._resample_size[1]
    )


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run()
