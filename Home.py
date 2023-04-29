
import base64
from time import sleep
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
import cv2
import qrcode
from io import BytesIO







st.sidebar.markdown("")
st.title(f'Home', )

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url('https://i.imgur.com/qtgYw2X.jpg');
    background-size: cover;
    background-repeat: no-repeat;
}}
[data-testid="stSidebar"] > div:first-child {{
    background-image: url("https://i.imgur.com/8zYaTBO.jpg");
    background-position: center;
    background-size: 150%;
   }}

</style>
"""

code = '''def hello():
print("Hello, friend...I'm Julian and I'm learning Python")'''
st.code(code, language='python')
st.markdown(page_bg_img, unsafe_allow_html=True)
image = Image.open('sideProfile.jpg')
st.image(image, width=900) 
st.markdown("<h1 style='text-align: center; color: white; style=font-style: oblique'>I GRIEVE IN STEREO</h1>",  unsafe_allow_html=True)
st.markdown('<p style="font-family:arial-black; font-size: 60px;"></p>', unsafe_allow_html=True)
audio_file = open('LDA.ogg.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')



# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add the URL to the QR code object
qr.add_data('https://twitter.com/SlyTheSky')

# Generate the QR code
qr.make(fit=True)

# Create an image from the QR code data
img = qr.make_image(fill_color="black", back_color="white")
img.save('myfile.png')
st.image(img)

# Convert the image object to a bytes-like object
img_bytes = BytesIO()
img.save(img_bytes, format='PNG')
img_bytes = img_bytes.getvalue()