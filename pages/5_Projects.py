import streamlit as st
from streamlit_extras.mention import mention
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

st.header("Projects", divider="red")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "projects.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

faceid = Image.open("assets/faceid.jpg")
sl = Image.open("assets/sign-language.jpg")
foot = Image.open("assets/foot.jpg")

with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("YOLOv8 Object Detection for Football", divider="blue")
        st.write("*Self-initiated project*")
        st.markdown("""
            - ► Imported from roboflow a custom dataset containing 1,327 images annotated with four distinct classes: player, ball, referee, and goalkeeper.
            - ► Trained a YOLOv8 object detection pretrained model on this custom dataset achieving 0.86 mAP50 on the validation set.
        """)
        mention(label="Github Repo", icon="github", url="https://github.com/issamjebnouni/YOLOv8-Object-Detection-for-Football")

    with image_column:
        st.image(foot)

with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("Building a Siamese Neural Network for Face Verification", divider="blue")
        st.write("*Self-initiated project*")
        st.markdown("""
            - ► Built a Siamese network, specifically designed for comparing similarities. With twin subnetworks generating 
            embeddings and a tailored loss function, it excelled in facial recognition.
            - ► By crafting a training dataset, incorporating data augmentation, and utilizing VGGFace for feature 
            extraction, I improved the model’s accuracy. 
            - ► The Siamese architecture, coupled with a custom training loop, yielded remarkable average recall and 
            precision on the test set — 99% and 100% respectively.
            - ► Real-time testing demonstrated the model’s practical utility.
        """)
        mention(label="Streamlit App", icon="streamlit", url="https://facial-verification.streamlit.app/")
        mention(label="Github Repo", icon="github", url="https://github.com/issamjebnouni/Facial-Verification")

    with image_column:
        st.image(faceid)


with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("Arabic Word-level Sign Language Recognition", divider="blue")
        st.write("*End of Year project*")
        st.markdown("""
            - ► Worked on the largest dataset for word-level Arabic sign language recognition, containing 502 words 
            performed by three signers. I used the 100 words subset of this dataset for experiments.
            - ► Leveraged mediapipe's holistic model to extract the hand and pose landmarks and used them to train a 
            Bidirectional LSTM model. Setting Adam optimizer, categorical_crossentropy loss and categorical_accuracy metric.
            - ► Achieved 99.6% accuracy on the test set and 0.026 loss.
            - ► Examined the generalization ability of our model, testing its performance with unseen persons and under 
            different conditions. This exploration uncovered areas for improvement, which we will focus on in the future.
        """)
        mention(label="Github Repo", icon="github", url="https://github.com/issamjebnouni/Arabic-Word-level-Sign-Language-Recognition")

    with image_column:
        st.image(sl)