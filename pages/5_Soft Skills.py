import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "education.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.header("Soft Skills", divider="red")
with st.container():
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown(f'<p style="font-size: 20px;">Problem Solving</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 20px;">Leadership</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 20px;">Communication</p>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<p style="font-size: 20px;">Emotional Intelligence</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 20px;">Persuasion</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 20px;">Collaboration</p>', unsafe_allow_html=True)