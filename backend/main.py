from fastapi import FastAPI, File, UploadFile
import uvicorn
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

app = FastAPI()
model = load_model('./ml/model_cnn.h5')


def preprocess(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("L").resize((28, 28))
    arr = np.array(img) / 255.0
    return np.expand_dims(arr, axis=(0, -1))

fashion_labels = {
    0: "T-shirt/top", 1: "Trouser", 2: "Pullover", 3: "Dress", 4: "Coat",
    5: "Sandal", 6: "Shirt", 7: "Sneaker", 8: "Bag", 9: "Ankle boot"
}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img_bytes = await file.read()
    img = preprocess(img_bytes)
    prediction = model.predict(img).argmax()
    label = fashion_labels[prediction]
    return {"prediction": int(prediction), "label": label}


# ...existing code...

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
# ...existing code...