import streamlit as st
from PIL import Image

st.title("*Photo and Video Uploader*")
st.header("Upload Photo")
uploaded_photo = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])
if uploaded_photo is not None:
    photo = Image.open(uploaded_photo)
    
    val=st.text_input("Image Description",max_chars=120)
    st.image(photo, caption=val, use_column_width=True)
    
