import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

st.header("Experience", divider="red")

datadoit = Image.open("assets/datadoit.png")
onetech = Image.open("assets/onetech.png")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "projects.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with st.container():
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(datadoit)
    with text_column:
        st.subheader("Computer Vision Intern @ [DataDoIt](https://data-doit.com/)")
        st.write("*Jul 2023 - Aug 2023*")
        st.markdown("""
        - ► Developed a flask application.
        - ► Utilised Nvidia TAO Toolkit and experimented on different models for object detection.
        
        `Python` `Orange Pi` `Flask` `NVIDIA TAO` `YOLO`
        """)