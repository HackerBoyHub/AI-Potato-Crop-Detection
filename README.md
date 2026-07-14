# AI-Potato-Crop-Detection
CNN-based potato leaf disease detection using TensorFlow, Flask, and PlantVillage dataset.
<img width="764" height="898" alt="image" src="https://github.com/user-attachments/assets/274426d6-0588-4072-a3d3-d4e98088f8ae" />
as You Can see prediciton  it Does
# AI Potato Crop Detection 🌿

AI Potato Crop Detection is a deep learning-based web application that detects potato leaf diseases from uploaded images. The project uses a Convolutional Neural Network (CNN) trained on the PlantVillage dataset and is deployed using Flask.

## Features

- Detects potato leaf diseases from leaf images.
- Classifies images into:
  - Healthy
  - Early Blight
  - Late Blight
- User-friendly web interface built with Flask.
- Displays prediction along with confidence score.
- Fast and accurate image classification.

## Technologies Used

- Python 3
- TensorFlow / Keras
- Flask
- HTML
- CSS
- NumPy
- Pillow (PIL)
- Matplotlib

## Dataset

This project uses the **PlantVillage** dataset for training and evaluation.

Classes:
- Potato___Healthy
- Potato___Early_Blight
- Potato___Late_Blight


## Installation

### Clone the repository

```bash
git clone https://github.com/HackerBoyHub/AI-Potato-Crop-Detection.git
cd AI-Potato-Crop-Detection
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## How It Works

1. Upload a potato leaf image.
2. The image is resized and normalized.
3. The trained CNN model predicts the disease.
4. The predicted class and confidence score are displayed on the webpage.

## Model

- Model: Convolutional Neural Network (CNN)
- Framework: TensorFlow / Keras
- Dataset: PlantVillage
- Classes: 3
- Accuracy: Approximately **95%+**

## Future Improvements

- Mobile application using TensorFlow Lite.
- Multi-crop disease detection.
- Real-time camera detection.
- Disease severity prediction.
- Cloud deployment.
- Treatment recommendations.

## Author

**Ismail Jabri**

B.Tech Student | Data Science & AI Enthusiast
