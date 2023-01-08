from flask import Flask, render_template, request, jsonify
import qrcode
import io
import os

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')




qr_image = None

@app.route('/generate', methods=['POST'])
def generate():
    global qr_image
    text = request.form['text']
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="#2c7dfa")
    
    # Save the image to a temporary file
    file_path = 'static/image/qr.png'
    img.save(file_path)
    
    # Set the global qr_image variable to the URL of the image
    qr_image = 'static/image/qr.png'
    
    # Render the homepage template
    return render_template('index.html', qr_image = qr_image)


@app.errorhandler(405 or 404)
def resource_not_found(e):
    return jsonify(error=str(e))

app.run(debug=True)



