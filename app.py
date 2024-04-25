import os
from flask import Flask, request, render_template
import cv2

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def pencil_sketch(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=230.0)
    return pencil_sketch


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    file = request.files['image']
    if file:
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(img_path)

        image = cv2.imread(img_path)
        sketch = pencil_sketch(image)

        sketch_path = os.path.join(app.config['UPLOAD_FOLDER'], 'sketch_' + file.filename)
        cv2.imwrite(sketch_path, sketch)

        return render_template('index.html', image_path=img_path, sketch_path=sketch_path)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
