import streamlit as st


with st.form('my form'):
    st.write('Temukan IMT (BMI) Anda dan risiko kesehatan')     
    berat, tinggi, umur = st.columns(3)
    with berat:
        berat = st.number_input('Berat Badan ', 0)

    with tinggi:
        tinggi = st.number_input('Tinggi Badan', 0)
    
    with umur:
        umur = st.number_input('Usia', 0)

    hasil = st.form_submit_button("Check Hasil")