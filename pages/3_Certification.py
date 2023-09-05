import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

st.header("Certifications", divider="red")

coursera = Image.open("assets/coursera.png")
datacamp = Image.open("assets/datacamp.jpg")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "certification.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    
with st.container():

    image_column, text_column = st.columns((1,2.5))
    with image_column:
        st.image(coursera)

    with text_column:
        st.subheader("[Machine Learning Specialization](https://www.coursera.org/account/accomplishments/specialization/certificate/73QUF3UXV7KU)", divider="blue")
        st.markdown("""
            - ► In the first course, I learned about linear regression, logistic regression, cost functions, and the gradient descent 
            algorithm.
            - ► In the second course, I was introduced to more advanced learning algorithms, including neural networks,
            decision tree ensembles. I also gained insights into key machine learning concepts such as bias and 
            variance, cross-validation, and improving learning algorithms' efficiency.
            - ► In the final course I got introduced to clustering algorithms, anomaly detection algorithms, collaborative filtering
            and content-based filtering, and in the last week, reinforcement learning.
            """, )

with st.container():

    image_column, text_column = st.columns((1,2.5))
    with image_column:
        st.image(datacamp)

    with text_column:
        st.subheader("[Data Scientist with Python Career Track](https://www.datacamp.com/statement-of-accomplishment/track/28f0e84562ad94ff677d6d10563bf65231cc510f)", divider="blue")
        st.write('''
                 - ► I learned how this versatile language allows you to import, clean, manipulate,
                 and visualize data: all integral skills for any aspiring data professional or researcher. 
                 - ► As I progressed, I worked with real-world datasets to learn the statistical and machine-learning 
                 techniques needed to perform hypothesis testing and build predictive models. 
                 - ► I also got an introduction to supervised learning with scikit-learn and applied my skills to various projects 
                 provided on the platform.
                 ''')

with st.container():

    image_column, text_column = st.columns((1,2.5))
    with image_column:
        st.image(datacamp)

    with text_column:
        st.subheader("[Python Programmer Career Track](https://www.datacamp.com/statement-of-accomplishment/track/29b51b71ac3ecb95396ded748049cd86d583c4b2)", divider="blue")
        st.write('''
                 - ► In this track, I learned how to manipulate data, write efficient Python code, and work with
                 challenging data, including date and time data, text data, and web data using APIs. 
                 - ► As my skills grew, I progressed to writing Python functions and unit testing—an essential skill needed to find
                 bugs in your code before your users do! 
                 - ► Through interactive exercises, I gained experience working with powerful Python libraries, including NumPy, pytest, and pycodestyle, that helped me perform
                 key programmer tasks such as web development, data analysis, and task automation.
                 ''')