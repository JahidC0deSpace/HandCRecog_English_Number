import cv2
import numpy as np
from keras.models import load_model
import os
import base64
import re

# --- Global variables to load model and map only once ---
MODEL_PATH = 'HCR_English_updated.h5'
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at '{MODEL_PATH}'. Please ensure it's in the correct directory.")

try:
    HCR_MODEL = load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    raise IOError(f"Error loading the model: {e}")

WORD_DICT = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I',
    19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R',
    28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z',
    36: 'a', 37: 'b', 38: 'c', 39: 'd', 40: 'e', 41: 'f', 42: 'g', 43: 'h', 44: 'i',
    45: 'j', 46: 'k', 47: 'l', 48: 'm', 49: 'n', 50: 'o', 51: 'p', 52: 'q', 53: 'r',
    54: 's', 55: 't', 56: 'u', 57: 'v', 58: 'w', 59: 'x', 60: 'y', 61: 'z'
}

def preprocess_image(image_array, is_drawing=False):
    """Preprocesses an image numpy array for the EMNIST model."""
    # The drawing canvas will have a transparent background (4 channels RGBA)
    # We need to convert it to grayscale.
    if is_drawing:
        # The canvas background is transparent (alpha=0), character is black (alpha=255)
        # We use the alpha channel as our grayscale image.
        if image_array.shape[2] == 4:
            img_gray = image_array[:, :, 3]
        else: # Fallback for RGB images
            img_gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    else:
        img_gray = image_array

    # Resize and apply adaptive thresholding
    img_resized = cv2.resize(img_gray, (28, 28), interpolation=cv2.INTER_AREA)
    img_binary = cv2.adaptiveThreshold(
        img_resized, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )
    
    # Invert colors
    img_inverted = cv2.bitwise_not(img_binary)
    
    # Normalize and reshape
    img_normalized = img_inverted.astype('float32') / 255.0
    img_final = img_normalized.reshape(1, 28, 28, 1)
    
    return img_final

def predict_character_from_path(image_path):
    """Predicts the character from a given image file path."""
    img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img_gray is None:
        raise ValueError(f"Image at path '{image_path}' could not be read.")
        
    processed_image = preprocess_image(img_gray, is_drawing=False)
    
    prediction = HCR_MODEL.predict(processed_image)
    predicted_index = np.argmax(prediction)
    predicted_char = WORD_DICT.get(predicted_index, "Unknown")
    
    return predicted_char

def predict_character_from_drawing(base64_data):
    """Decodes a base64 image string and predicts the character."""
    # Remove the header from the base64 string
    img_str = re.search(r'base64,(.*)', base64_data).group(1)
    
    # Decode the image
    img_decoded = base64.b64decode(img_str)
    
    # Convert to a numpy array
    np_arr = np.frombuffer(img_decoded, np.uint8)
    
    # Read the image data with alpha channel
    img_np = cv2.imdecode(np_arr, cv2.IMREAD_UNCHANGED)
    
    if img_np is None:
        raise ValueError("Could not decode the drawing image data.")

    # Preprocess the numpy array from the drawing
    processed_image = preprocess_image(img_np, is_drawing=True)

    prediction = HCR_MODEL.predict(processed_image)
    predicted_index = np.argmax(prediction)
    predicted_char = WORD_DICT.get(predicted_index, "Unknown")

    return predicted_char
