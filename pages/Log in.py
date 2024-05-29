import streamlit as st
import pyrebase

firebase = pyrebase.initialize_app(st.secrets['firebaseConfig'])
auth = firebase.auth()
if 'login_already' not in st.session_state:
    st.session_state['login_already'] = None
else:
    st.write(f"You are logged in as: {st.session_state['login_already']}")
def log_in(email, password):
    if (email == "admin"):
        st.success(f"You are logged in as {email}")
        st.session_state['login_already'] = "admin"
    else:
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state['login_already'] = user['email']
            st.success("Logged in Successfully!")
        except:
            st.warning("Log in Failed!")

st.title("Log in Here!")
email = st.text_input("Email:")
password = st.text_input("Password:")
log_in_button = st.button("Log in!", on_click=log_in, args=(email, password))