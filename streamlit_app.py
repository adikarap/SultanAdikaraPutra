import streamlit as st

st.title("Sultan Adikara Putra")
st.write(
    "Hallo guys, nama aku Sultan Adikara Putra aku sekola di SMAN 20 Bandung."
)

st.image("view/IMG_3948.png")

st.header("aplikasi mengecek Nilai Genap/Ganjil")
angka = st.number_input("tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan Genap")
else: 
    st.write(f"{angka} adalah bilangan Ganjil")
