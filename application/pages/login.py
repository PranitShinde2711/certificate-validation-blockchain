
import streamlit as st
from db.firebase_app import login
from streamlit_extras.switch_page_button import switch_page
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

# If profile is not set in session state, let the user choose their profile type.
if "profile" not in st.session_state:
    profile = st.selectbox("Select your profile", ["Institute", "Verifier"])
    st.session_state.profile = profile

form = st.form("login")
email = form.text_input("Enter your email")
password = form.text_input("Enter your password", type="password")

# Provide an option for new users to navigate to the registration page.
if st.button("New user? Click here to register!"):
    switch_page("register")

submit = form.form_submit_button("Login")
if submit:
    result = login(email, password)
    if result == "success":
        st.success("Login successful!")
        # Switch page based on profile type.
        if st.session_state.profile == "Institute":
            switch_page("institute")
        else:
            switch_page("verifier")
    else:
        st.error("Invalid credentials!")