import streamlit as st
from PIL import Image

st.title ("Que emoción, mi primera app :D")
st.header ("En este espacio comienzo a desarrollar mis apps para interfases")
st.write ("Facilmente puedo realizar backend y frontend")
image = Image.open ('gaton.jpg')
st.image (image, caption = 'que felicidad')

texto = st.text_input ('escribiendo algo, no sé que escribir, ojalá ser ese gato' , 'gatote feliz y coqueton')
st.write ('el texto escritoes', texto)
