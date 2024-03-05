import streamlit as st
from PIL import Image
from pathlib import Path
from utils import social_icons

st.set_page_config(page_title="My Portfolio", 
                   page_icon=":rocket:", 
                   layout="wide")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "Issam_Jebnouni_Resume.pdf"
css_file = current_dir / "styles" / "homepage.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

img = Image.open("assets/pfp4.png")

with st.container():
    left_column, middle_column, right_column = st.columns((1,0.2,0.6))
    with left_column:
        st.header("About Me", divider='red')
        st.subheader("Aspiring Computer Vision Student")
        st.write("- 👋🏻 Hi, I'm Issam! I'm a Computer vision undergraduate student based in Tunisia. Having prior relevant experiences in computer vision and being in my final year, I am constantly seeking a 6-month end of studies internship to broaden my horizons before embarking on my career upon graduation.")
        st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream")
        st.markdown(social_icons(32, 32, LinkedIn="https://www.linkedin.com/in/issamjebnouni/", 
                                         GitHub="https://github.com/issamjebnouni", 
                                         Medium="https://medium.com/@issam.jebnouni"),
                                         unsafe_allow_html=True)
    with middle_column:
        st.empty()
    with right_column:
        st.image(img)

