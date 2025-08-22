from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
from prediction import predict_character_from_path, predict_character_from_drawing

# Initialize the Flask application
app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Checks if the uploaded file has an allowed extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the image upload and prediction."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request.'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No image selected for uploading.'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            predicted_char = predict_character_from_path(filepath)
            return jsonify({'prediction': predicted_char})
        except Exception as e:
            return jsonify({'error': f'An error occurred during prediction: {str(e)}'}), 500
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)
    else:
        return jsonify({'error': 'Allowed image types are -> png, jpg, jpeg, bmp'}), 400

@app.route('/predict_drawing', methods=['POST'])
def predict_drawing():
    """Handles the drawing canvas data and prediction."""
    data = request.get_json()
    if 'imageData' not in data:
        return jsonify({'error': 'No image data received.'}), 400
    
    image_b64 = data['imageData']
    
    try:
        predicted_char = predict_character_from_drawing(image_b64)
        return jsonify({'prediction': predicted_char})
    except Exception as e:
        return jsonify({'error': f'An error occurred during prediction: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
