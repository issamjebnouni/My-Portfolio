import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

st.header("Education", divider="red")

insat = Image.open("assets/INSAT.jpg")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "education.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with st.container():

    image_column, text_column = st.columns((1,2.5))
    with image_column:
        st.image(insat, width=200, caption="National Institute of Applied Sciences and Technology")

    with text_column:
        st.write("### Bachelor Degree, [_INSAT_](https://insat.rnu.tn) (2019-2024)")
        st.write("##### Major: Computer Science")
        st.write("##### Minor: Image and Video Processing")
        st.write("**Relevant Coursework:** Linear Algebra, Algorithms and Data Structures, Machine learning, Deep Learning, Big Data, Business Intelligence, Image Processing, Video Processing, Linux...")