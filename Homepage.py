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


'''
# ---- Self Description ----
with st.container():
   st.write("---")
   st.header("A Little Bit About Me")
   st.write("##")
   text_column, image_column = st.columns((1, 2)) #st.columns((1, 2))
   with text_column:
       st.subheader("A Personal Favorite")
       st.write(
           """
           I am a huge Black Panther fan! I love him throughout just about all of his adaptations from the "King of the Dead" Black Panther we see in
           Jonathan Hickman's Avengers and New Avengers comics to the more mellowed king we saw in the MCU, and even his adaptation in the cartoon Avengers: Earth's Mightiest Heroes!
           I love how he has to balance balancing being a superhero for all people while still needing to prioritize Wakanda.
           """
       )
   with image_column:
       st.image(img_blackpanther)
       st.markdown("[Where This Awesome Black Panther Image Comes From](https://www.marvel.com/comics/issue/40474/fantastic_four_1998_608)")
with st.container():
   image_column, text_column  = st.columns((2, 1)) #st.columns((2, 1))
   with text_column:
       st.subheader("Another Favorite")
       st.write(
           """
           I also love Thor comics and some of his main movies.
           I think Thor's story arc is quite amazing. From being an arrogant, prideful warrior who is by all means unfit to be a leader of any kind
           to being an Avenger who's willing to sacrifice his own life to save the people he cares about the most.
           I also find it quite fascinating that this character who is quite stoic in nature also struggles with self worth when it comes to Mjolnir.
           The idea that despite all of Thor's accomplishments and feats of strengths still struggling to see himself as worthy or proving to Odin that he is worthy is pretty unique.
           """
       )
   with image_column:
       st.image(img_thor)
       st.markdown("[Where This Legendary Thor Image Comes From](https://www.marvel.com/comics/issue/89743/thor_2020_23)")


'''


with st.container():
   st.markdown('<h1 style="text-align: center;">Contact Me</h1>', unsafe_allow_html=True)
   st.write("---")
   st.write("##")


   st.markdown('<div style="text-align: justify;"> <font size = "4"> - Email: PLACEHOLDER@PLACEHOLDER.com </font> </div>', unsafe_allow_html=True)
   st.markdown('<div style="text-align: justify;"> <font size = "4"> - Linkedin: PLACEHOLDER link </font> </div>', unsafe_allow_html=True)
   st.markdown('<div style="text-align: justify;"> <font size = "4"> - Github: PLACEHOLDER link </font> </div>', unsafe_allow_html=True)
   st.write("---")  

