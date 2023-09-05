from pathlib import Path
from PIL import Image
import streamlit as st
from utils import social_icons

st.set_page_config(layout="centered")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir.parent / "assets" / "resume.pdf"
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
- ► Image Processing
- ► Machine Learning, Deep Learning
- ► Programming languages: Python
- ► Libraries & Frameworks: Tensorflow, Keras, streamlit, Flask, OpenCV, Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn, Pillow
- ► Tools: Nvidia TAO, mediapipe, YOLO
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
- **Relevant Coursework:** Linear Algebra, Algorithms and Data Structures, Machine learning, Deep Learning, Big Data, Business Intelligence, Image Processing, Video Processing.
"""
)


# --- WORK EXPERIENCE ---
st.write('\n')
st.subheader("Work Experience", divider="red")

st.write(
    """
Computer Vision Intern @ [DataDoIt](https://data-doit.com/)

*Jul 2023 - Aug 2023*

- ► Developed a flask application.

- ► Utilised Nvidia TAO Toolkit and experimented on different models for object detection.

- `Python` `Orange Pi` `Flask` `NVIDIA TAO` `YOLO`
        """)

# --- PROJECTS ---
st.write('\n')
st.subheader("Projects", divider="red")

# --- Project 2
st.write(
    """
Building a Siamese Neural Network for Face Verification

*Self-initiated project*

- ► Built a Siamese network, specifically designed for comparing similarities. With twin subnetworks generating 
embeddings and a tailored loss function, it excelled in facial recognition.

- ► By crafting a training dataset, incorporating data augmentation, and utilizing VGGFace for feature 
extraction, I improved the model’s accuracy. 

- ► The Siamese architecture, coupled with a custom training loop, yielded remarkable average recall and 
precision on the test set — 99% and 100% respectively.

- ► Real-time testing demonstrated the model’s practical utility.
    """)


# --- Project 1
st.write('\n')
st.write(
    """
Arabic Word-level Sign Language Recognition

*End of Year project*

- ► Worked on the largest dataset for word-level Arabic sign language recognition, containing 502 words 
performed by three signers. I used the 100 words subset of this dataset for experiments.

- ► Leveraged mediapipe's holistic model to extract the hand and pose landmarks and used them to train a 
Bidirectional LSTM model. Setting Adam optimizer, categorical_crossentropy loss and categorical_accuracy metric.

- ► Achieved 99.6% accuracy on the test set and 0.026 loss.

- ► Examined the generalization ability of our model, testing its performance with unseen persons and under 
different conditions. This exploration uncovered areas for improvement, which we will focus on in the future.
    """)

# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("Certifications", divider="red")

# --- Certification 3
st.write(
    """
[Machine Learning Specialization](https://www.coursera.org/account/accomplishments/specialization/certificate/73QUF3UXV7KU)

- ► In the first course, I learned about linear regression, logistic regression, cost functions, and the gradient descent 
algorithm.
- ► In the second course, I was introduced to more advanced learning algorithms, including neural networks,
decision tree ensembles. I also gained insights into key machine learning concepts such as bias and 
variance, cross-validation, and improving learning algorithms' efficiency.
- ► In the final course I got introduced to clustering algorithms, anomaly detection algorithms, collaborative filtering
and content-based filtering, and in the last week, reinforcement learning.
    """)

# --- Certification 2
st.write(
    """
[Data Scientist with Python Career Track](https://www.datacamp.com/statement-of-accomplishment/track/28f0e84562ad94ff677d6d10563bf65231cc510f)

- ► I learned how this versatile language allows you to import, clean, manipulate,
and visualize data: all integral skills for any aspiring data professional or researcher. 
- ► As I progressed, I worked with real-world datasets to learn the statistical and machine-learning 
techniques needed to perform hypothesis testing and build predictive models. 
- ► I also got an introduction to supervised learning with scikit-learn and applied my skills to various projects 
provided on the platform.
    """)
# --- Certification 1
st.write(
    """
[Python Programmer Career Track](https://www.datacamp.com/statement-of-accomplishment/track/29b51b71ac3ecb95396ded748049cd86d583c4b2)

- ► In this track, I learned how to manipulate data, write efficient Python code, and work with
challenging data, including date and time data, text data, and web data using APIs. 
- ► As my skills grew, I progressed to writing Python functions and unit testing—an essential skill needed to find
bugs in your code before your users do! 
- ► Through interactive exercises, I gained experience working with powerful Python libraries, including NumPy, pytest, and pycodestyle, that helped me perform
key programmer tasks such as web development, data analysis, and task automation.
    """)

# --- EXTRACURRICULAR ACTIVITIES ---
st.write('\n')
st.subheader("Extracurricular Activities", divider="red")

# --- Activity 4
st.write(
    """
Head of Public and Industry Relations @ [IEEE TUNISIA SECTION](https://ieee.tn)

*Apr 2023 – Present*
- ► Joined the core team of the Taskforce for Efficient Organizational Units Accounting.

- ► This project supported by the IEEE Tunisia Section will improve the experience of 30+ student branches and their subunits.

- ► This year-long project aims to restructure the communication flow among all the units and subunits with the section and reduce unnecessary emails and phone calls by more than 50%.
    """)

# --- Activity 3
st.write(
    """
Head of Sponsorship of the IEEE R8 SYP Congress @ [IEEE INSAT STUDENT BRANCH](https://insat.ieee.tn)

*Feb 2022 – Aug 2022*

- ► Won the right to organize IEEE EMEA Region Student and Young Professional Congress in Tunisia.

- ► Raised approximately 30,000$ from local and international sponsors to fund the congress.

- ►  Managed the participation of 200+ attendees and guests during the 5-day Congress.
    """)

# --- Activity 2
st.write(
    """
General Secretary @ [IEEE Computer Society Chapter INSAT](https://cs-insat.ieee.tn/)

*Sep 2021 – May 2022*

- ►  Scheduled and coordinated executive board meetings, ensuring efficient operation of the chapter.

- ►   Supported the organization of 3 significant events, contributing to their successful execution.
    """)


# --- Activity 1
st.write(
    """
Ambassador / Project Manager @ [IEEE Computer Society Chapter INSAT](https://cs-insat.ieee.tn/)

*Apr 2021 – Oct 2021*

- ►  This was the fifteenth edition of the international competetitive programming hackathon IEEEXtreme.

- ►  Managed a committee to organize a highly successful edition of the hackathon, attracting 160 participants.

- ►  Communicated essential information provided by regional ambassadors, facilitating effective coordination.
    """)