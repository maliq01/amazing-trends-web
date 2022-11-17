from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie




st.set_page_config(page_title="amazing trends", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#loading css file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

local_css("style/style.css")

#load assets
lottie_codding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_A9xmVE.json")
dera_swift = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_gEXLbi.json")
air_force_1 = Image.open("images/air.png")
air_force_red = Image.open("images/82-827757_white-sneakers-png-clipart-nike-air-force-1.png")


#---header and description--
with st.container():
    st.subheader("Who are we?")
    st.title("Amazing trends")
    st.write("""
    we are a one stop shop for all your shoes and dera needs. We not only make you look good but we also make every step an adventure
    
    our dedicated team ensures that you get the value for your money. with:
    
    -ever present customer service.
    
    -prompt delivery 
    
    -easy way to make an order
    
    we are with you every step of the way. Always.
    """)
    st.write("[view shoes catalogue >](https://www.instagram.com/p/Ckpiqj1IqjO/?igshid=YmMyMTA2M2Y=)")
    st.write("are also sell Deras ")
    st.write("[view dera catalogue >](https://www.instagram.com/p/CeqWldQIP7k/?igshid=YmMyMTA2M2Y=)")
#shoes catalogue
with st.container():
    st.write("---")
    left_column , right_column = st.columns(2)
    with left_column:
        st.header("Shoes")
        st.write("##")
        st.write(
            """
            we are a shoe and  online shop who sell new and quality products.

            -we deliver for free within the Nairobi cbd area
            
            -we also do international and national shipping
            
            -we are trusted and verified with most of the local and international brands
            
            -With our shoes every step you take is an adventure.
            """
            )
    with right_column:
        st_lottie(lottie_codding, height = 300, key = "codding")
#dera catalogue

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Deras")
        st.write("##")
        st.write(
            """
            we also sell beautiful and quality Deras for all sizes.

            -we deliver for free within the Nairobi cbd area

            -we also do international and national shipping

            -we are trusted and verified with most of the local and international brands
            """
        )
    with right_column:
        st_lottie(dera_swift, height=300, key="dera")


# project
with st.container():
    st.write("---")
    st.header("our products")
    st.write("##")
    image_column , txt_column = st.columns((1, 2))
    with image_column:
        st.image(air_force_1)
    with txt_column:
        st.subheader(" Nike air force 1")
        st.write("white airforce 1 in stock shop now")
        st.subheader("$20")
with st.container():
    image_column , txt_column = st.columns((1,2))
    with image_column:
        st.image(air_force_red)
    with txt_column:
        st.subheader("Nike red shoes")
        st.write("white and red airforce in stock")
        st.subheader("$35")
#contact info.
with st.container():
    st.write("---")
    st.subheader("contact us")
    st.write("##")
    contact_form ="""<form action="https://formsubmit.co/wanjikumwaura98@gmail.com" method="POST">
     <input type = "hidden" name ="captcha" value ="false">
     <input type="text" name="name" placeholder= "your name" required>
     <input type="email" name="email" placeholder = "your email" required>
     <textarea name= "message" placeholder = "your message" required></textarea>
     <button type="submit">Send</button>
</form>
"""
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html = True)
    with right_column:
        st.empty()






        

