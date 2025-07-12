import streamlit as st

def about():
    st.title("Portfolio Saya")
    st.header("Data Scientist")
    st.write('Nama saya eva dari kelas Dibimbing DS-32-A yang saat ini sedang mengerjakan tugas ' \
    'Portofolio Building with Streamlit. Saya alumni Statistika ITS yang saat ini bekerja di perusahaan swasta di Surabaya ' \
    'sebagai Procurement Analyst')

    st.title("Kontak")
    st.write("Hubungi saya melalui tautan berikut:")

    # LinkedIn
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/evamusdalifah/)"
    )

    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/evamusdalifah/)"
    )

    # Email
    st.write("📧 Email: evamusdalifah04@example.com")