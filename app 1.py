import streamlit as st

st.title("こんにちは、吉村ゼミ")
name = st.text_input("好きな人はなんですか")

st.write(name) 

camera_photo = st.camera_imput("ハイチーズ!") 
if camera:
  st.image(camera, caption="写真",use_column_width=True)
  
