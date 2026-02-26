import streamlit as st
from PIL import Image

st.title ("Que emoción, mi primera app :D")
st.header ("En este espacio comienzo a desarrollar mis apps para interfases")
st.write ("Facilmente puedo realizar backend y frontend")
image = Image.open ('gaton.jpg')
st.image (image, caption = 'que felicidad')

texto = st.text_input ('escribe algo, no sé como que ojalá ser ese gato' , 'gatote feliz y coqueton')
st.write ('el texto escrito es', texto)

st.subheader ("Ahora usemos dos columnas")
col1 , col2 = st.columns (2)


with col1:
  st.subheader ('caracteristicas de un gato feliz y coqueton')
  st.write (" se ve muy feliz y es bien coqueton")
  resp = st.checkbox ('Cierto?')
  if resp:
    st.write ('total')


with col2:
  st.subheader ('cosas que no le gustan a un gato feliz y coqueton')
  modo = st.radio (" que no le den sus buenas croquetas con:" , ('salsita' , 'pollito' , 'aguita' ))
        if modo == 'salsita':
           st.write ('preferiblemente de pescadito')       
        if modo == 'pollito':
           st.write ('del almuerzo de su dueño')    
         if modo == 'aguita':
           st.write ('muy simple, considera las otras opciones')       
          
