import streamlit as st
import pyrebase
firebase = pyrebase.initialize_app(st.secrets['firebaseConfig'])
auth = firebase.auth()
if 'login_already' not in st.session_state:
    st.session_state['login_already'] = None
else:
    st.write(f"You are logged in as: {st.session_state['login_already']}")
def sign_up(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        if user:
            auth.send_email_verification(user['idToken'])
        st.success("Signed up successfully!")
    except:
        st.warning("Sign Up Failed!")

st.title("Sign Up Here!")
email = st.text_input("Email:")
password = st.text_input("Password:")
log_in_button = st.button("Sign up!", on_click=sign_up, args=(email, password))