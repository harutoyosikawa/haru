import streamlit as st

st.title("こんにちは、吉村ゼミ")

name = st.text_input("名前を入力")

st.write(name) 

st.checkbox("同意します")
adress = st.selectbox("次の中から現住所を教えてください",["京都","大阪","兵庫"])
st.write(adress)

hobby = st.multiselect("趣味を次から複数選択してください",["音楽","運動","勉強"])
st.write(hobby)

st.slider("この映画を10点満点で評価してください",0,10,0)

camera = st.camera_input("写真を撮影します!") 
if camera:
  st.image(camera, caption="写真",use_column_width=True)
  
