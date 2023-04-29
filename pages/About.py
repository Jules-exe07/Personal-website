import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests
import glob



st.markdown("")
st.sidebar.markdown("")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# --- load images ---
lottie_ima = load_lottieurl ('https://assets7.lottiefiles.com/packages/lf20_gssu2dkm.json')
music_vis = load_lottieurl ('https://assets9.lottiefiles.com/packages/lf20_vixkj2dq.json')


st.title(f'Personal & Projects')
st.write('I am currently studying web development using Python. I work for an Insurance company in the U.S but I work from home in South America.')
st_lottie(lottie_ima, height=300, width=600)


st.write('I like to use AI to create images based on the prompt, this is a very cool way to be created using the power of AI. ' 'Here you can find some of those images [Gallery](https://twitter.com/SlyTheSky)')

@st.cache(allow_output_mutation=True)

def load_images():
    image_files = glob.glob("AI Dreams/*/*.png")
    manuscripts = []
    for image_file in image_files:
        image_file = image_file.replace("\\", "/")
        parts = image_file.split("/")
        if parts[1] not in manuscripts:
            manuscripts.append(parts[1])
    manuscripts.sort()

    return image_files, manuscripts

st.title("Some dreams")
image_files, manuscripts = load_images()
view_manuscripts = st.multiselect("Select Manuscript(s)", manuscripts)
n = st.number_input("Select Grid Width", 1, 5, 3)

view_images = []
for image_file in image_files:
    if any(manuscript in image_file for manuscript in view_manuscripts):
        view_images.append(image_file)
groups = []
for i in range(0, len(view_images), n):
    groups.append(view_images[i:i+n])

for group in groups:
    cols = st.columns(n)
    for i, image_file in enumerate(group):
        cols[i].image(image_file)


st.subheader('Music')
st.write('I will like to make music when Im old, my dream is having a studio at my place')
st_lottie(music_vis, height=300, width=600)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url('https://i.imgur.com/9VmgvEx.jpg');
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

st.markdown(page_bg_img, unsafe_allow_html=True)

