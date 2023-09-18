from pathlib import Path
from PIL import Image
import streamlit as st
from utils import social_icons

st.set_page_config(layout="centered")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir.parent / "assets" / "Issam_Jebnouni_Resume.pdf"
profile_pic = current_dir.parent / "assets" / "pfp3.png"
css_file = current_dir.parent / "styles" / "resume.css"

# --- LOAD PDF, PROFILE PIC & CSS ---

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
# --- HERO SECTION ---
with st.container():
    left_column, middle_column, right_column = st.columns((1,0.2,1))
    
    with left_column:
        st.image(profile_pic)

    with middle_column:
        st.empty()

    with right_column:
        st.title("Issam Jebnouni")
        st.write("Computer Vision Undergraduate student.")
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", "issam.jebnouni@insat.ucar.tn")
        st.write("📱", "+216 56 511 577")
        st.markdown(social_icons(32, 32, LinkedIn="https://www.linkedin.com/in/issamjebnouni/",
                                         GitHub="https://github.com/issamjebnouni",
                                         Medium="https://medium.com/@issam.jebnouni"),
                                         unsafe_allow_html=True)


# --- Skills ---
st.write('\n')
st.subheader("Hard Skills", divider="red")
st.write(
    """
- ► Image and Video Processing
- ► Machine Learning, Deep Learning, Computer Vision
- ► Operating Systems: Linux
- ► Programming languages: Python
- ► Libraries & Frameworks: Tensorflow, Keras, streamlit, Flask, OpenCV, Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn, Pillow
- ► Tools: Nvidia TAO, mediapipe, YOLOv8
"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("Education", divider="red")

st.write(
    """
### Bachelor Degree, [INSAT](https://insat.rnu.tn) (2019-2024)
- ##### Major: Computer Science
- ##### Minor: Image and Video Processing
- **Relevant Coursework:**  Machine learning, Deep Learning, Image and Video Processing, Big Data, Business Intelligence, Linux.
"""
)


# --- WORK EXPERIENCE ---
st.write('\n')
st.subheader("Work Experience", divider="red")

st.write(
    """
**Computer Vision Intern @ [DataDoIt](https://data-doit.com/)**

*Jul 2023 - Aug 2023*

- ► Developed a web application with Flask which scans multiple camera streams in the local network and displays them.
- ► Experimented with and benchmarked multiple object detection models in the Nvidia TAO Toolkit.
- ► Trained YOLOv8 model on the same task using a mixture of synthetic and real data and validated on real data only. Using this approach achieved 96% validation mAP50.
""")

# --- PROJECTS ---
st.write('\n')
st.subheader("Projects", divider="red")

# --- Project 3
st.write(
    """
**∎ YOLOv8 OBJECT DETECTION FOR FOOTBALL**

*Self-initiated project*

- ► Fitted a YOLOv8 object detection model on a custom football dataset featuring four classes,
 achieving 86% mAP50 on the validation set after 25 epochs.
    """)


# --- Project 2
st.write(
    """
**∎ FACIAL VERIFICATION MODEL USING A SIAMESE NETWORK**

*Self-initiated project*

- ► Crafted a training dataset, incorporated data augmentation to expand it to 3000 images.

- ► Built a Siamese neural network, tailored for comparing similarities using Tensorflow’s Functional API that yielded remarkable average recall and precision on the test set:  99% and 100% respectively.
    """)


# --- Project 1
st.write('\n')
st.write(
    """
**∎ ARABIC WORD-LEVEL SIGN LANGUAGE RECOGNITION MODEL**

*End of Year project*

- ► Extracted Hand and Pose Keypoints from sign videos of 100 arabic words using Mediapipe's Holistic Model.

- ► Trained a BiLSTM model on the extracted features and achieved 99.62% accuracy on test data.
    """)

# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("Certifications", divider="red")

# --- Certification 3
st.write(
    """
∎ [Machine Learning Specialization](https://www.coursera.org/account/accomplishments/specialization/certificate/73QUF3UXV7KU)
    """)

# --- Certification 2
st.write(
    """
∎ [Data Scientist with Python Career Track](https://www.datacamp.com/statement-of-accomplishment/track/28f0e84562ad94ff677d6d10563bf65231cc510f)
    """)
# --- Certification 1
st.write(
    """
∎ [Python Programmer Career Track](https://www.datacamp.com/statement-of-accomplishment/track/29b51b71ac3ecb95396ded748049cd86d583c4b2)
    """)

# --- EXTRACURRICULAR ACTIVITIES ---
st.write('\n')
st.subheader("Extracurricular Activities", divider="red")


st.write(
    """
**∎ Head of Sponsorship of the IEEE R8 SYP Congress @ [IEEE INSAT STUDENT BRANCH](https://insat.ieee.tn)**

*Feb 2022 – Aug 2022*

- ► Organized the IEEE EMEA Region Student and Young Professional Congress in Tunisia that attracted 200 participants.

- ► Raised approximately 30,000$ from local and international sponsors to fund the congress.
    """)

# --- Activity 2
st.write(
    """
**∎ General Secretary @ [IEEE Computer Society Chapter INSAT](https://cs-insat.ieee.tn/)**

*Sep 2021 – May 2022*

- ► Scheduled and coordinated meetings of an 8-people executive board, ensuring efficient operation of the chapter.

- ► Supported the organization of 3 significant events, contributing to their successful execution.
    """)


# --- Activity 1
st.write(
    """
**∎ Ambassador / Project Manager @ [IEEE Computer Society Chapter INSAT](https://cs-insat.ieee.tn/)**

*Apr 2021 – Oct 2021*

- ► Served as one of 700+ ambassadors around the world to communicate essential information to my student branch. 

- ► Managed a committee to organize a highly successful edition of the hackathon, attracting 160 participants.
    """)
