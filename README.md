Handwriting Character Recognition Web AppThis project is a web application that uses a Convolutional Neural Network (CNN) to recognize handwritten characters (letters and numbers). Users can either upload an image of a character or draw one directly on a canvas in the browser to get a real-time prediction from the trained model.
<br>
✨Features<br>
Dual Input Methods:<br>
Image Upload: Users can upload .png, .jpg, or .jpeg files.<br>
Live Drawing Canvas: A responsive HTML5 canvas allows users to draw characters with a mouse or touch input.<br>
Deep Learning Model: Utilizes a CNN built with Keras (TensorFlow backend) trained on the EMNIST (ByClass) dataset.<br>
Real-Time Prediction: The Flask backend processes the input and returns the model's prediction to the user without a page refresh.<br>
Clean User Interface: A simple, modern, and intuitive UI with tabs for easy navigation between the two input methods.<br>
🛠️ Tech Stack<br>
Backend: Python, Flask<br>
Machine Learning: TensorFlow, Keras, scikit-learn<br>
Image Processing: OpenCV, Pillow<br>
Frontend: HTML5, CSS3, JavaScript (with Fetch API)Data Handling: NumPy, Pandas<br>
📂 File StructureThe project is organized into the following structure:<br>
hcr_flask_app/<br>
├── app.py                   # Main Flask application routes<br>
├── prediction.py            # Image processing and model prediction logic<br>
├── HCR_English_updated.h5   # The trained Keras model file<br>
├── README.md                # This README file<br>
└── templates/<br>
    └── index.html           # Frontend HTML template<br>
└── static/<br>
    └── style.css            # CSS for styling the web page<br>
└── uploads/                 # Temporary folder for uploaded images<br>

🚀 Setup and InstallationFollow these steps to get the application running on your local machine.
1. PrerequisitesPython 3.8+pip (Python package installer)
2. 2. Clone the Repositorygit clone [https://your-repository-url.com/hcr_flask_app.git](https://your-repository-url.com/hcr_flask_app.git)
cd hcr_flask_app

3. Install DependenciesIt is highly recommended to use a virtual environment to manage project dependencies.# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the required packages
pip install Flask tensorflow keras opencv-python Pillow

4. Place the Model FileEnsure that your trained model file, HCR_English_updated.h5, is placed in the root directory of the project (hcr_flask_app/).🏃‍♂️ How to RunStart the Flask Server:Open your terminal, navigate to the project's root directory, and run the following command:python app.py

Access the Application:Once the server is running, open your web browser and go to the following URL:[http://127.0.0.1:5000](http://127.0.0.1:5000)

🧠 Model DetailsThe recognition model is a Convolutional Neural Network (CNN) with the following architecture:Conv2D Layer (32 filters, ReLU)Conv2D Layer (64 filters, ReLU)MaxPooling2D & DropoutConv2D Layer (128 filters, ReLU)MaxPooling2D & DropoutFlatten LayerDense Layer (256 units, ReLU) & DropoutDense Layer (512 units, ReLU) & DropoutOutput Dense Layer (62 units, Softmax)It was trained on the EMNIST (ByClass) dataset, which contains 62 classes of uppercase letters, lowercase letters, and digits.🤝 ContributingContributions are welcome! If you have suggestions for improvements, please feel free to fork the repository and submit a pull request.Fork the ProjectCreate your Feature Branch (git checkout -b feature/AmazingFeature)Commit your Changes (git commit -m 'Add some AmazingFeature')Push to the Branch (git push origin feature/AmazingFeature)Open a Pull Request📜 LicenseThis project is licensed under the MIT License. See the LICENSE file for more details.
