import cv2
import streamlit as st
import numpy as np 
from PIL import Image
import base64
# from torch import square
#from streamlit_lottie import st_lottie  # pip install streamlit-lottie
#import json



###############################################################################
def cartoonization (img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray = cv2.medianBlur(gray, 9) 
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
 										cv2.THRESH_BINARY, 9, 9)
    
    color = cv2.bilateralFilter(img, 5, 100, 100) 
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

try:
    one, two = st.columns(2)
    with one:
        file_image = st.camera_input(label = "Take a pic of you to be sketched out")
        input_img = Image.open(file_image)
        final_sketch = cartoonization(np.array(input_img))
    with two:
        st.write("**Output Sketch**")
        st.image(final_sketch, use_column_width=True)     
except AttributeError:
  print("Variable x is not defined")






