import streamlit as st
from PIL import Image


img = Image.open('squarelogo.png')
st.set_page_config(page_title="Face Cartoonizer",page_icon=img,layout="wide")


st.markdown("<h1 style='text-align: Center; color: red;font-size:60px;'>Facial Cartoonizer!</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: black ;font-size:50px;'>Cartoons aren’t just for kids. Try our cartoonizer to inspire fresh, fun, colorful creations.</h1>", unsafe_allow_html=True)

st.write("---")

image = Image.open('compare.png')


with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(image)

    with text_col:
        st.subheader("Cartoonize a Picture With Just One Click")
        st.markdown("<h1 style='text-align: justify; color: black;font-size:20px;'>Facial Cartoonizer allows you to turn photo into cartoon images like a professional artist. In just one click, you can cartoonize photos and get amazing print-level cartoon pictures of landscapes, pets, food and more.Cartoon art presents a great way to make yourself more approachable and fun across your social media presence. With Facial Cartoonizer, you can turn picture into cartoon and get astounding cartoon art right before your eyes..</h1>", unsafe_allow_html=True)

st.write("---")
st.write("##")

with st.container():
    st.markdown("<h1 style='text-align: center; color: black;font-size:20px;'>Did you know that cartoons go all the way back to the Middle Ages? That was the term used to describe sketches made by artists before they embarked upon the serious work of creating their masterpieces. By the 19th Century, Punch magazine used it as shorthand for satirical illustrations. Somehow, cartoons eventually became what we know and love them as today. But enough of the history lesson. You want to learn how to turn your photos into cartoons. Well, you’ve come to the right place. Better yet, Picsart has a whole bunch of styles and effects available. From pop art to pencil drawing, surreal and artistic, you can transform any photo into a cartoon in a flash. Ready to put some fun into your photographs?</h1>", unsafe_allow_html=True)



# [theme]
# primaryColor = "#E694FF"
# secondaryBackgroundColor = "#00172B"
# backgroundColor = "#0083B8"
# textColor = "#C6CDD4"
