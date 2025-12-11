import streamlit as st

st.title("Berapakah Jumlah Rukun Iman?")

# tab1, tab2 = st.tabs(["Soal Rukun Iman", "Soal Rukun Islam"])
# with tab1:
#     st.write("Rukun Iman Ada berapa hayoooo?")
# with tab2:
#     st.write("Rukun Islam ada berapa yaaa?")
    

st.sidebar.title("Menu Samping")
pilihan = st.sidebar.selectbox("Pilih menu", ["Rukun Iman", "Profil", "Kontak"])





st.button("7", key="7", width=600)
st.button("6", key="6", width=600)
st.button("5", key="5", width=600)
st.button("4", key="4", width=600)


# if st.button("4"):
#     st.success("Benar")
# else:
#     st.error("Salah")

# import streamlit as st

# def page_1():
#     st.title("Page 1")
#     st.page_link("page_2.py", query_params={"utm_source": "page_1"})

# pg = st.navigation([page_1, "page_2.py"])
# pg.run()