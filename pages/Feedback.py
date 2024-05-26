import streamlit as st
import streamlit_survey as ss
if 'login_already' not in st.session_state:
    st.session_state['login_already'] = None

st.title('Feedback')
survey = ss.StreamlitSurvey('Feedback Form')
if st.session_state['login_already'] == None:
    st.warning("Log in First!")
else:
    pages = survey.pages(1, on_submit=lambda: st.success('Your response has been recorded. Thank you for your time!'))
    pages.submit_button = lambda pages: st.button('Submit', type='primary', use_container_width=True)

    with pages:
        if pages.current == 0:
            survey.dateinput('Date:')
            st.write(
                'How satisfied are you with our app?')
            st.radio(
                'satisfied', options=['😡', '☹️', '😀', '😍'], index=0, label_visibility='collapsed', horizontal=True
            )
            survey.text_area('How did we do today?')
