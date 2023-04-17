import streamlit as st
#import pandas as pd
#from PIL import video

st.header("Upload Video")
uploaded_video = st.file_uploader("Choose a video", type=["mp4","mov"]) 
if uploaded_video is not None:
     st.video(uploaded_video)
     st.caption("video uploaded ")