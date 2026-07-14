from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("potato_disease_model.keras")

# Class names
class_names = [
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy"
]

IMAGE_SIZE = 256

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Read image
    img = Image.open(filepath).convert("RGB")

    # Resize
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))

    # Convert to numpy
    img = np.array(img)

    # Normalize
    img = img / 255.0

    # Add batch dimension
    img = np.expand_dims(img, axis=0)

    # Prediction
    prediction = model.predict(img)

    predicted_index = np.argmax(prediction[0])

    predicted_class = class_names[predicted_index]

    confidence = round(100 * np.max(prediction[0]), 2)

    return render_template(
        "index.html",
        prediction=predicted_class,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)