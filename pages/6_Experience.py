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
        - ► Developed a Flask-based web interface for scanning and displaying local network RTSP camera streams.
        - ► Explored the NVIDIA TAO toolkit 4.0 then trained and benchmarked various object detection models from its vast model zoo, achieving 0.90 mAP for the best model which was YOLOv4.
        - ► Explored methods for enhancing model precision with limited real data, settling on training on mixed data (real + synthetic) and validating on real data only.
        - ► Achieved a 0.96 mAP50 on the validation set using the YOLOv8 model with mixed data and generated a TensorRT engine to optimize the model for inference.
                    
        `Python` `Linux` `Flask` `NVIDIA TAO` `YOLOv8`
        """)