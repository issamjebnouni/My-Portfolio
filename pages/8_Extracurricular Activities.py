import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "projects.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.header("Extracurricular Activities", divider="red")

ieee = Image.open('assets/ieee_tn.png')
cs = Image.open('assets/cs.png')
insat = Image.open('assets/ieee_insat.png')

with st.container():
    text_column, mid, image_column = st.columns((3,0.4,1))
    with text_column:
        st.subheader("Head of Public and Industry Relations", divider="blue")
        st.write("*Apr 2023 – Present*")
        st.markdown("""
        - ► Joined the core team of the Taskforce for Efficient Organizational Units Accounting.
        - ► This project supported by the IEEE Tunisia Section will improve the experience of 30+ student branches and their subunits.
        - ► This year-long project aims to restructure the communication flow among all the units and subunits with the section and reduce unnecessary emails and phone calls by more than 50%.
                    """)
    with mid:
        st.empty()
    with image_column:
        st.image(ieee, caption="IEEE Tunisia Section")

with st.container():
    text_column, mid, image_column = st.columns((3,0.4,1))
    with text_column:
        st.subheader("Head of Sponsorship of the IEEE R8 SYP Congress", divider="blue")
        st.write("*Feb 2022 – Aug 2022*")
        st.markdown("""
        - ► Won the right to organize IEEE EMEA Region Student and Young Professional Congress in Tunisia.
        - ► Raised approximately 30,000$ from local and international sponsors to fund the congress.
        - ►  Managed the participation of 200+ attendees and guests during the 5-day Congress.
                    """)
    with mid:
        st.empty()
    with image_column:
        st.image(insat, caption="IEEE INSAT Student Branch")

with st.container():
    text_column, mid, image_column = st.columns((3,0.4,1))
    with text_column:
        st.subheader("General Secretary", divider="blue")
        st.write("*Sep 2021 – May 2022*")
        st.markdown("""
        - ► Scheduled and coordinated executive board meetings, ensuring efficient operation of the chapter.
        - ►  Supported the organization of 3 significant events, contributing to their successful execution.
        """)
    with mid:
        st.empty()
    with image_column:
        st.image(cs, caption="IEEE Computer Society Chapter INSAT")

with st.container():
    text_column, mid, image_column = st.columns((3,0.4,1))
    with text_column:
        st.subheader("Ambassador / Project Manager", divider="blue")
        st.write("*Apr 2021 – Oct 2021*")
        st.markdown("""
        - ► This was the fifteenth edition of the international competetitive programming hackathon IEEEXtreme.
        - ► Managed a committee to organize a highly successful edition of the hackathon, attracting 160 participants.
        - ► Communicated essential information provided by regional ambassadors, facilitating effective coordination.
        """)
    with mid:
        st.empty()
    with image_column:
        st.image(cs, caption="IEEE Computer Society Chapter INSAT")