import io
import numpy as np
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model("model/model.h5")

# Define class names (modify as per your dataset)
class_names = ["Early Blight", "Late Blight", "Healthy"]  # Update with actual class names

app = FastAPI()

# Function to preprocess the image
def preprocess_image(image: Image.Image):
    image = image.resize((256, 256))  # Resize to match model input size
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Expand dims for batch
    return image

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Read and convert image
        image = Image.open(io.BytesIO(await file.read()))
        image = preprocess_image(image)

        # Predict using model
        predictions = model.predict(image)
        confidence = float(np.max(predictions)) * 100  # Get confidence percentage
        predicted_class = int(np.argmax(predictions))
        class_label = class_names[predicted_class]

        return {"predicted_class": class_label, "confidence": f"{confidence:.2f}%"}

    except Exception as e:
        return {"error": str(e)}

# Run using: uvicorn app:app --host 0.0.0.0 --port 8000

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

    