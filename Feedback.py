import streamlit as st
import streamlit_survey as ss

st.title('Feedback')
survey = ss.StreamlitSurvey('Feedback Form')
pages = survey.pages(1, on_submit=lambda: st.success('Your response has been recorded. Thank you for your time!'))
pages.submit_button = lambda pages: st.button('Submit', type='primary', use_container_width=True)
pages.prev_button = lambda pages: None
with pages:
    if pages.current == 0:
        survey.dateinput('Date:')
        st.radio(
            'How satisfied are you with our app features?', options=['😡', '☹️', '😀', '😍'], index=0, label_visibility='collapsed', horizontal=True
        )   
        survey.text_area('How did we do today?')
