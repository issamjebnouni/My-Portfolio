import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "education.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.header("Hard Skills", divider="red")

def txt3(a, b):
  col1, col2 = st.columns([2,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

st.markdown(f'<p style="font-size: 20px;">Deep Learning, Computer Vision, Docker</p>', unsafe_allow_html=True)

txt3("Operating Systems","`Linux`")
txt3("Programming languages","`Python`")
txt3("Libraries & Frameworks","`Ultralytics`, `Detectron2`, `MMDetection`, `Tensorflow`, `Keras`, `Streamlit`, `Flask`, `OpenCV`, `Pandas`, `Numpy`, `Matplotlib`, `Seaborn`, `Scikit-learn`, `Pillow`")
txt3("Tools","`Nvidia TAO`, `mediapipe`, `YOLOv8`")
