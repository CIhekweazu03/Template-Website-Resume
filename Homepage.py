import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="PLACEHOLDER's Resume", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_mu1asgg9.json")
img_1 = Image.open("images/img_1.jpg")
img_2 = Image.open("images/img_2.jpg")



# ---- HEADER SECTION ----
with st.container():
    st.title("Hi, I am PLACEHOLDER :sunglasses:")
    st.subheader("I'm a student majoring in PLACEHOLDER at PLACEHOLDER")
    st.write(
        "My personal hobbies include PLACEHOLDER, PLACEHOLDER, and of course, more PLACEHOLDER!"
    )

# ---- WHAT IS THIS ABOUT ----
with st.container():
    #st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What Exactly Is This For?")
        st.write("##")
        st.write(
            """
            This website serves an easy way to keep up with my personal projects, experiences, etc. in a way a traditional one page resume cannot.
            """
        )
    with right_column:
        st.image(img_1)
    st.write("---")

# ---- Self Description ----
with st.container():
    st.markdown('<h1 style="text-align: center;">Education</h1>', unsafe_allow_html=True)
    st.write("---")
    st.write("##")
    
    st.markdown('<h3 style="text-align: center;">Basic Info</h3>', unsafe_allow_html=True)
    #st.markdown('<h2 style="text-align: center;">____________</h2>', unsafe_allow_html=True)

    st.markdown('<div style="text-align: justify;"> <font size = "4"> - Student at PLACEHOLDER University </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> <font size = "4"> - Major: PLACEHOLDER </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> <font size = "4"> - GPA: 4.0 </font> </div>', unsafe_allow_html=True)
    st.write("---")   

with st.container():

    st.markdown('<h3 style="text-align: center;"> Organizations and Extracurriculars </h3>', unsafe_allow_html=True)
    

    st.markdown('<div style="text-align: justify;"> <font size = "4"> Currently involved with: </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> <font size = "4"> - PLACEHOLDER ORGANIZATION, 2020 - Present </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> <font size = "4"> - PLACEHOLDER 2, 2021 - Present </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> <font size = "4"> Previously involved with: </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> <font size = "4"> - PLACEHOLDER ORGANIZATION, 2019 - 2022 </font> </div>', unsafe_allow_html=True)
    st.write("---")


with st.container():


    st.markdown('<h1 style="text-align: center;">Work Experiences</h1>', unsafe_allow_html=True)
    st.write("---")
    st.write("##")
    

    st.markdown('<div style="text-align: justify;"> <font size = "4"> - Worked on PLACEHOLDER at PLACEHOLDER using PLACEHOLDER. 2020 - Present </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> <font size = "4"> - Implemented on PLACEHOLDER at PLACEHOLDER ORGANIZATION using PLACEHOLDER AND PLACEHOLDER. 2019 - 2022 </font> </div>', unsafe_allow_html=True)
    st.write("---")

with st.container():
    st.markdown('<h1 style="text-align: center;">Technical Skills</h1>', unsafe_allow_html=True)
    st.write("---")
    st.write("##")

    st.markdown('<div style="text-align: justify;"> <font size = "4"> - Programming Languages: PLACEHOLDER. </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> <font size = "4"> - Experience working on PLACEHOLDER, PLACEHOLDER, and PLACEHOLDER. </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> <font size = "4"> - Technical coursework: PLACEHOLDER AND PLACEHOLDER </font> </div>', unsafe_allow_html=True)
    st.write("---")   


with st.container():
    st.markdown('<h1 style="text-align: center;">Contact Me</h1>', unsafe_allow_html=True)
    st.write("---")
    st.write("##")

    st.markdown('<div style="text-align: justify;"> <font size = "4"> - Email: PLACEHOLDER@PLACEHOLDER.com </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> <font size = "4"> - Linkedin: PLACEHOLDER link </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;"> <font size = "4"> - Github: PLACEHOLDER link </font> </div>', unsafe_allow_html=True)
    st.write("---")   
