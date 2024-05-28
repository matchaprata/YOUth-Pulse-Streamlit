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

with st.expander('Type of Feedback'):    
    col1, col2, col3, col4 = st.columns(4)
    with col1: 
        userexp = st.button('User Experience') 
    if userexp: 
        with pages:
            if pages.current == 0:
                    survey.dateinput('Date:')
                    st.write(
                        'How satisfied are you with our app?')
                    st.radio(
                        'satisfied', options=['😡', '☹️', '😀', '😍'], index=0, label_visibility='collapsed', horizontal=True
                    )
                    survey.text_area('How did we do today?')
                    survey.text_area('Are there any other current affairs topics you would like to see being implemented in the discussions held?')

    with col2:
        qna = st.button('Q&A')
    if qna:
        st.write(
            'hello world'
        )