import streamlit as st
st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman",
                        ["About", "Project"])


if page == 'About' :
    import about
    about.about()
elif page == 'Project' : 
    import project
    project.projectsatu()