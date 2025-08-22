# 📘 Project Title

_A brief one-liner summarizing the project._

> Optional tagline or short project description.

---

## ✨ Features

- ✅ Image Upload: Users can upload .png, .jpg, or .jpeg files.
- ✅ Live Drawing Canvas: A responsive HTML5 canvas allows users to draw characters with a mouse or touch input.
- ✅ Utilizes a CNN built with Keras (TensorFlow backend) trained on the EMNIST (ByClass) dataset.
- ✅ The Flask backend processes the input and returns the model's prediction to the user without a page refresh.
- ✅ A simple, modern, and intuitive UI with tabs for easy navigation between the two input methods.

---

## 🛠️ Tech Stack

| Category       | Technologies                               |
|----------------|--------------------------------------------|
| **Backend**    | Flask, Python                              |
| **ML Library** | TensorFlow, Keras                          |
| **Frontend**   | HTML5, CSS3, JavaScript                    |
| **Image Proc.**| OpenCV, Pillow                             |
| **Data**       | EMNIST Dataset                             |

---

## 📁 Project Structure
project-root/ <br>
├── app.py # Entry point: Flask server <br>
├── prediction.py # Model inference & image processing <br>
├── HCR_English_updated.h5 # Trained CNN Model <br>
├── templates/<br>
│ └── index.html # Frontend HTML page<br>
├── static/<br>
│ └── style.css # Custom CSS <br>
├── uploads/ # Uploaded image files<br>
├── README.md # Project documentation<br>
└── requirements.txt # Python dependencies<br>

---

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.8+
- `pip` package manager

### 🧪 Installation

# Clone the repository
git clone https://github.com/JahidC0deSpace/HandCRecog_English_Number.git
cd your-project

# Create a virtual environment
- python -m venv venv
- source venv/bin/activate  # Or use venv\Scripts\activate on Windows

# Install dependencies
- pip install -r requirements.txt
🤖 Model Setup
- Ensure the file HCR_English_updated.h5 (your trained model) is in the root folder.
python app.py

🧠 Model Architecture
Briefly explain your deep learning model:

- Conv2D → ReLU → Conv2D → MaxPooling → Dropout
- Conv2D → ReLU → MaxPooling → Dropout
- Flatten → Dense (256, ReLU) → Dropout
- Dense (512, ReLU) → Dropout
- Dense (62, Softmax)
Trained on EMNIST (ByClass) dataset: 62 character classes (A–Z, a–z, 0–9)
📌 Usage
- Upload Image: Choose an image file from your system.
- Draw on Canvas: Use your mouse or touchscreen.
- Predict: Model gives real-time prediction.
🪪 License
- This project is licensed under the MIT License.
See the LICENSE file for more information.
🙋‍♂️ Contact
Created by Md. Jahid Hasan Jitu — feel free to reach out!
Open issues or suggestions via GitHub Issues
