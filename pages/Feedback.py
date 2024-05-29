import streamlit as st
import streamlit_survey as ss
import streamlit.components.v1 as components
from datetime import datetime

if 'login_already' not in st.session_state:
    st.session_state['login_already'] = None

st.title('Feedback')
survey = ss.StreamlitSurvey('Feedback Form')
if st.session_state['login_already'] == None:
    st.warning("Log in First!")
else:
    pages = survey.pages(1, on_submit=lambda: st.success('Your response has been recorded. Thank you for your time!'))
    tab1, tab2 = st.tabs(["User Experience", "Q&A"])
    with pages:
        if pages.current == 0:
            pages.submit_button = lambda pages: st.button('Submit', type='primary', use_container_width=True)
            with tab1:
                survey.dateinput('Date:', key="UX")
                st.write(
                    'How satisfied are you with our app?')
                st.radio(
                    'satisfied', options=['😡', '☹️', '😀', '😍'], index=0, label_visibility='collapsed', horizontal=True
                )
                survey.text_area('How did we do today?')
                survey.text_area('Do you have any suggestions to improve our website?')
            with tab2:
                col1, col2, col3, col4, col5 = st.columns(5)
                surveyType = ""
                with col1:
                    st.button('Education')
                with col2:
                    st.button('Environment')
                with col3:
                    st.button('Budget 2024')
                if col1:
                    surveyType = "Education"
                if col2:
                    surveyType = "Environment"
                if col3:
                    surveyType = "Budget 2024"

                survey.dateinput('Date:', key="Q&A")
                survey.text_area('Is there anything you would like to clarify about in your chosen category?')