import streamlit as st
import streamlit_survey as ss
import streamlit.components.v1 as components
from itertools import cycle

def ChangeButtonColour(widget_label, prsd_status):
    htmlstr = ""
    for i in range(len(btn_labels)):
        btn_bg_colour = pressed_colour if prsd_status[i] == True else unpressed_colour
        htmlstr += f"""
            <script>
                var elements = window.parent.document.querySelectorAll('button');
                for (var i = 0; i < elements.length; ++i) {{ 
                    if (elements[i].innerText == '{widget_label[i]}') {{ 
                        elements[i].style.background = '{btn_bg_colour}'
                    }}
                }}
            </script>
            """
    components.html(f"{htmlstr}", height=0, width=0)

def btn_pressed_callback(i):
    mystate.btn_prsd_status = [False] * len(btn_labels)
    mystate.btn_prsd_status[i-1] = True

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
        
        mystate = st.session_state
        if "btn_prsd_status" not in mystate:
            mystate.btn_prsd_status = [False] * 2

        btn_labels = ["User Experience", "Q&A"]
        unpressed_colour = "#adb5bd"
        pressed_colour = "#6f42c1"

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            col11 = st.button(btn_labels[0], key="b1", on_click=btn_pressed_callback, args=(1,) )
        with col2:
            col22 = st.button(btn_labels[1], key="b2", on_click=btn_pressed_callback, args=(2,) )

        if col11:
            with pages:
                if pages.current == 0:
                    survey.dateinput('Date:')
                    st.write(
                        'How satisfied are you with our app?')
                    st.radio(
                        'satisfied', options=['😡', '☹️', '😀', '😍'], index=0, label_visibility='collapsed', horizontal=True
                    )
                    survey.text_area('How did we do today?')
                    survey.text_area('Do you have any suggestions to improve our website?')
                ChangeButtonColour(btn_labels, mystate.btn_prsd_status)
                
                   
        
        if col22:
            with pages:
                if pages.current == 0:
                    survey.dateinput('Date:')
                    st.write(
                        'How satisfied are you with our app?')
                    st.radio(
                        'satisfied', options=['😡', '☹️', '😀', '😍'], index=0, label_visibility='collapsed',
                        horizontal=True
                    )
                    survey.text_area('How did we do today?')
                    survey.text_area(
                        'Are there any other current affairs topics you would like to see being implemented in the discussions held?')
                ChangeButtonColour(btn_labels, mystate.btn_prsd_status)



