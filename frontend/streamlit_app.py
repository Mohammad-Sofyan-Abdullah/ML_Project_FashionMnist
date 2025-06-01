import streamlit as st
import requests

st.title("Fashion Item Classifier")
file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if file:
    res = requests.post("http://127.0.0.1:8000/predict", files={"file": file.getvalue()})
    data = res.json()
    st.success(f"Prediction: {data['label']} (class {data['prediction']})")
if st.button("Clear"):
    st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], key="clear")
    st.success("Cleared the uploaded image.")