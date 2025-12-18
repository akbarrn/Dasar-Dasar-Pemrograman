import streamlit as st

st.title('Quiz Islami')
st.sidebar.title("Quiz Islami Pilihan")
menu = st.sidebar.selectbox("Pilih Soal", ["Rukun Iman", "Rukun Islam", "Nabi & Rasul", "Sifat Wajib Bagi Rasul"])
        
if "menu_sebelumnya" not in st.session_state:
    st.session_state.menu_sebelumnya = None

if menu != st.session_state.menu_sebelumnya:
    st.session_state.current_soal = 0
    st.session_state.score = 0
    st.session_state.koreksi = None
    st.session_state.menu_sebelumnya = menu
    
if menu == 'Rukun Iman':
    st.session_state.soal = [
        {"soal": "Berapa jumlah rukun iman?", "options": ["6", "4", "5","25"],
         "jawaban": "6"},
        {"soal": "Kitab suci yang diturunkan kepada Nabi Musa AS adalah", "options": ['Zabur', 'Taurat', 'Injil', 'Al-Quran'],
         "jawaban": "Taurat"},
        {"soal": "Percaya bahwa segala sesuatu terjadi atas kehendak Allah disebut iman kepada ", "options": ['Hari Akhir','Qada dan Qadar','Kitab Allah','Malaikat Allah'], 
        "jawaban": "Qada dan Qadar"},
        {"soal": "Malaikat yang menjaga Pintu Syurga adalah", "options": ["Malik", "Jibril", "Ridwan", "Mikail"],
         "jawaban": "Ridwan"},
        {"soal": "Berapa jumlah nabi & rasul yang wajib kita ketahui", "options": ["10", "15", "20", "25"], 
        "jawaban": "25"},
    ]

elif  menu == 'Sifat Wajib Bagi Rasul':
    st.session_state.soal = [
        {"soal": "Ada berapa Sifat Wajib bagi Rasul?" , "options": [ "3","4","5","6"],
         "jawaban": "4"},
        {"soal": "Rasul wajib memiliki sifat Tabligh yang artinya?", "options": ["Cerdas", "Berwibawa", "Menyampaikan", "Jujur"],
         "jawaban": "Menyampaikan"},
        {"soal": "Rasul tidak pernah berkhianat, selalu dapat dipercaya. Sifat wajib ini adalah", "options": ["Khianat","Tabligh", "Amanah","Biladah"], 
        "jawaban": "Amanah"},
        {"soal": "Rasul selalu berkata benar. Sifat wajib ini disebut", "options": ["Shiddiq", "Amanah", "Tabligh", "Fathonah"],
         "jawaban": "Shiddiq"},
        {"soal": "Rasul memiliki kecerdasan luar biasa sehingga mampu menjawab pertanyaan umat. Sifat wajib ini disebut", "options": ["Shiddiq", "Amanah", "Tabligh", "Fathonah"], "jawaban": "Fathonah"},
    ]
elif menu == 'Nabi & Rasul':
    st.session_state.soal = [
        {"soal": "Siapa Nabi yang termasuk Ulul Azmi?", "options": ["Ibrahim", "Yunus", "Adam", "Hud"], 
        "jawaban": "Ibrahim"},
        {"soal": "Nabi siapa yang mukjizatnya membuat kapal bahtera?", "options": ["Ilyas", "Idris", "Nuh", "Isa"], 
        "jawaban": "Nuh"},
        {"soal": "Nabi siapa yang diutus kepada kaum Tsamud dan diberi mukjizat keluar unta betina dari batu?", "options": ["Idris", "Sholeh", "Zakaria", "Muhammad SAW"], 
        "jawaban": "Sholeh"},
        {"soal": "Nabi siapa yang dibuang kedalam sumur oleh saudaranya?", "options": ["Yusuf", "Yunus", "Luth", "Ismail"], 
        "jawaban": "Yusuf"},
        {"soal": "Nabi siapa yang mukjizat nya Al-Qur'an?", "options": ["Musa", "Ishaq", "Ya'qub", "Muhammad SAW"], 
        "jawaban": "Muhammad SAW"}
    ]

elif menu == 'Rukun Islam':
    st.session_state.soal = [
        {"soal": "Rukun Islam yang pertama adalah", "options":['Syahadat', 'Salat', 'Zakat', 'Puasa'], 
        "jawaban": "Syahadat"},
        {"soal": "Mengucapkan dua kalimat syahadat berarti", "options":['Percaya kepada malaikat', 'Mengakui keesaan Allah dan kerasulan Nabi Muhammad SAW', 'Melaksanakan Puasa', 'Membayar zakat'], 
        "jawaban": "'Mengakui keesaan Allah dan kerasulan Nabi Muhammad SAW'"},
        {"soal": "Shalat Fardhu sehari semalam dilakukan sebanyak", "options":['Tiga', 'Empat', 'Lima', 'Enam'], 
        "jawaban": "Lima"},
        {"soal": "Zakat dikeluarkan oleh umat Islam, bagi yang?", "options":['Masih kecil','Mampu dan telah memenuhi syarat','Sedang bepergian','Belum baligh'], 
        "jawaban": "'Mampu dan telah memenuhi syarat'"},
        {"soal": "Puasa yang wajib, dilaksanakan pada bulan", "options":['Rajab','Syaban','Ramadhan','Zulhijah'], 
        "jawaban": "Ramadhan"},
       
    ]
if "current_soal" not in st.session_state:
    st.session_state.current_soal = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "koreksi" not in st.session_state:
    st.session_state.koreksi = None

def soal_fragment():
#    soal sama ambil respon user pake tombol

    soal_data = st.session_state.soal[st.session_state.current_soal]
    st.subheader(f"Soal {st.session_state.current_soal + 1}/{len(st.session_state.soal)}")
    st.write(soal_data['soal'])

    # tombol jawaban
    for option in soal_data['options']:
        if st.button(option, width=600):
            # Cek jawaban pas tombol diklik
            if option == soal_data['jawaban']:
                st.session_state.koreksi = ('success', 'Yeyyy Benar Bro')
                st.session_state.score += 1
            else:
                st.session_state.koreksi = ('error', f"Yah luu salah, yang bener tuhhh: {soal_data['jawaban']}")

            # Pindah soal
            if st.session_state.current_soal + 1 < len(st.session_state.soal):
                st.session_state.current_soal += 1
                st.rerun()
            else:
                st.session_state.current_soal = None
                st.rerun()  

def koreksi_fragment():
    
#    koreksi 
    if st.session_state.koreksi:
        msg_type, msg_content = st.session_state.koreksi
        if msg_type == "success":
            st.success(msg_content)
        elif msg_type == "error":
            st.error(msg_content)
        st.session_state.koreksi = None

koreksi_fragment()

if st.session_state.current_soal is not None:
    soal_fragment()
else:
    st.subheader('Quiz Selesai')
    total_soal = len(st.session_state.soal)
    benar = st.session_state.score
    nilai = int((benar / total_soal) * 100)
    # st.balloons()
    # st.snow()

    if "show_score" not in st.session_state:
        if st.button('Cek Skor'):
            st.session_state.show_score = True
            st.rerun()
    else:
        st.info(f'Kamu menjawab benar {benar} dari total {total_soal} soal.')
        st.write(f"Nilai: **{nilai}**")

    # if st.button('Cek Skor'):
    #     st.info(f'Kamu menjawab benar {benar} dari total {total_soal} soal.')
    #     st.write(f"Nilai: **{nilai}**")