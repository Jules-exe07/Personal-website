import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.markdown("")
st.sidebar.markdown("")
st.title('Contact us')
st.subheader('Leave us your comments below')


with st.form("form1", clear_on_submit=True):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter email address")
    message = st.text_area("Message")
    submit = st.form_submit_button("Submite this form")


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url('https://i.imgur.com/vByfaaU.jpg');
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

