import streamlit as st
from PIL import image
st.title ("Que emoción, mi primera app :D")
st.header ("En este espacio comienzo a desarrollar mis apps para interfases")
st.write ("Facilmente puedo realizar backend y frontend")
image = Image.open ('gaton.jpg')
st.image (image, caption = 'que felicidad')

