import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_login
from src.screens.student_screen import student_login


def main():

    if "login_type" not in st.session_state:
        st.session_state["login_type"] = "home"

    if st.session_state["login_type"] == "teacher":
        teacher_login()

    elif st.session_state["login_type"] == "student":
        student_login()

    else:
        home_screen()


main()