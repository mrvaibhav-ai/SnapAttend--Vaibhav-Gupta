import streamlit as st


def footer_home():

    st.markdown(
        """
        <div style="text-align:center; margin-top:35px; padding:15px;">
            <div style="
                display:inline-block;
                padding:10px 22px;
                border-radius:25px;
                background:rgba(255,255,255,0.10);
                border:1px solid rgba(255,255,255,0.18);
                color:white;
                font-family:Arial,sans-serif;
                font-size:15px;
                font-weight:600;
            ">
                Created with <span style="color:#ff4b6e;">♥</span> by
                <strong style="color:white;">Vaibhav Gupta</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def footer_dashboard():

    st.markdown(
        """
        <div style="text-align:center; margin-top:35px; padding:15px;">
            <div style="
                display:inline-block;
                padding:10px 22px;
                border-radius:25px;
                background:#ffffff;
                border:1px solid #e5e7eb;
                color:#555555;
                font-family:Arial,sans-serif;
                font-size:15px;
                font-weight:600;
            ">
                Created with <span style="color:#ff4b6e;">♥</span> by
                <strong style="color:#4f46e5;">Vaibhav Gupta</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )