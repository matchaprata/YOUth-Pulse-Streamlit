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
                survey.dateinput('Date:', key="Q&A")
                survey.text_area('Are there any other current affairs topics you would like to see being implemented in the discussions held?')