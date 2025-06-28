# 🥔 Potato Disease Classification using Deep Learning

This project provides an image classification API to detect potato leaf diseases using a trained CNN model built with TensorFlow and deployed using FastAPI.

---

## 📌 Features

- 🔍 Detects 3 classes of potato leaves:
  - Early Blight
  - Late Blight
  - Healthy
- 🚀 FastAPI backend for serving predictions
- 🧠 Pretrained Keras model (`model.h5`)
- 🧪 Easily testable using Postman or `curl`

---

## 📁 Project Structure

```
Potato-Disease-Classification-using-Deep-Learning/
├── api/
│   └── main.py                  # FastAPI app
├── dataset/
│   ├── Potato___Early_blight/   # Training/Validation Images
│   ├── Potato___healthy/
│   └── Potato___Late_blight/
├── model/
│   └── model.h5                 # Trained CNN model
├── Potato_Disease_Classification.ipynb  # Training notebook
├── requirements.txt            # Project dependencies
└── README.md
```

---

## 🚀 How to Run the API Locally

### 1️⃣ Navigate to the `api` folder

```bash
cd Potato-Disease-Classification-using-Deep-Learning/api
```

### 2️⃣ Install Dependencies

```bash
pip install -r ../requirements.txt
```

### 3️⃣ Run the FastAPI server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Then open [http://localhost:8000/docs](http://localhost:8000/docs) to test the API.

---

## 📬 API Usage

### Endpoint: `POST /predict/`

- **Form field**: `file` (image)
- **Response Example**:

```json
{
  "predicted_class": "Late Blight",
  "confidence": "93.45%"
}
```

---

## 📷 Test with curl

```bash
curl -X POST "http://localhost:8000/predict/" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path_to_your_image.jpg"
```

---

## ⚙️ Requirements

```
fastapi
uvicorn
tensorflow
numpy
pillow
aiofiles
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧠 Model Training

The model was trained using the dataset stored in the `dataset/` directory. You can retrain or fine-tune the model using the provided notebook:

```bash
Potato_Disease_Classification.ipynb
```

---

## 🛰 Deployment (Optional)

To deploy on **Render**:

- Push the repo to GitHub
- Create a new Web Service on [Render](https://render.com)
- Use the following:
  - **Build Command**: `pip install -r requirements.txt`
  - **Start Command**: `uvicorn api.main:app --host=0.0.0.0 --port=10000`

---

## 📜 License

MIT License — free to use and distribute
