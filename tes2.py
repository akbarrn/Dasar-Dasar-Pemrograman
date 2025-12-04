import streamlit as st
with st.form("form1"):
    name = st.text_input("Masukkan Nama")
    address = st.text_input("Masukkan Alamat")
    age = st.number_input("Masukkan Usia")
    submitted = st.form_submit_button("Kirim")
    

if submitted:
        st.write( name, address, age)