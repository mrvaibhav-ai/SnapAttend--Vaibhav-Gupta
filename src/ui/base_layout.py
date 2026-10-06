import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

        /* =========================
           HOME PAGE BACKGROUND
           ========================= */

        .stApp {
            background:
                radial-gradient(
                    circle at 15% 20%,
                    rgba(59, 130, 246, 0.22),
                    transparent 35%
                ),
                radial-gradient(
                    circle at 85% 80%,
                    rgba(99, 102, 241, 0.20),
                    transparent 35%
                ),
                linear-gradient(
                    135deg,
                    #0F172A 0%,
                    #172554 50%,
                    #1E1B4B 100%
                ) !important;

            min-height: 100vh;
        }


        /* =========================
           PORTAL CARDS
           ========================= */

        .stApp div[data-testid="stColumn"] {

            background: rgba(255, 255, 255, 0.08) !important;

            border: 1px solid rgba(255, 255, 255, 0.14) !important;

            padding: 2.5rem !important;

            border-radius: 2rem !important;

            box-shadow:
                0 20px 50px rgba(0, 0, 0, 0.22) !important;

            backdrop-filter: blur(14px);

            -webkit-backdrop-filter: blur(14px);

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;
        }


        /* =========================
           CARD HOVER
           ========================= */

        .stApp div[data-testid="stColumn"]:hover {

            transform: translateY(-5px);

            box-shadow:
                0 25px 60px rgba(0, 0, 0, 0.30) !important;
        }


                /* =========================
           HOME PAGE TEXT
           ========================= */

        .stApp [data-testid="stMarkdownContainer"] h1,
        .stApp [data-testid="stMarkdownContainer"] h2,
        .stApp [data-testid="stMarkdownContainer"] h3,
        .stApp [data-testid="stMarkdownContainer"] h4,
        .stApp [data-testid="stMarkdownContainer"] h5,
        .stApp [data-testid="stMarkdownContainer"] h6 {

            color: #FFFFFF !important;

            font-weight: 750 !important;

            text-shadow:
                0 2px 10px rgba(0, 0, 0, 0.30) !important;
        } 


        /* Portal titles */

        .stApp h1,
        .stApp h2 {

            font-weight: 750 !important;

            letter-spacing: -0.5px !important;

            text-shadow:
                0 2px 10px rgba(0, 0, 0, 0.25);
        }


        /* =========================
           DASHBOARD BACKGROUND
           ========================= */

        .dashboard-background {

            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(59, 130, 246, 0.10),
                    transparent 30%
                ),
                linear-gradient(
                    135deg,
                    #F8FAFC 0%,
                    #EEF2FF 50%,
                    #F8FAFC 100%
                );
        }


        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>

        /* =========================
           DASHBOARD BACKGROUND
           ========================= */

        .stApp {

            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(59, 130, 246, 0.10),
                    transparent 30%
                ),
                linear-gradient(
                    135deg,
                    #F8FAFC 0%,
                    #EEF2FF 50%,
                    #F8FAFC 100%
                ) !important;

            min-height: 100vh;
        }

        </style>
    """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>

        /* =========================
           GOOGLE FONT
           ========================= */

        @import url(
            'https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap'
        );


        /* =========================
           HIDE STREAMLIT UI
           ========================= */

        #MainMenu,
        footer,
        header {
            visibility: hidden;
        }


        /* =========================
           MAIN CONTAINER
           ========================= */

        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 2rem !important;
        }


        /* =========================
           GLOBAL FONT
           ========================= */

        h1,
        h2,
        h3,
        h4,
        h5,
        h6,
        p,
        span,
        label,
        div {
            font-family: 'Outfit', sans-serif;
        }


        /* =========================
           HEADINGS
           ========================= */

        h1 {
            font-size: 3.3rem !important;
            font-weight: 800 !important;
            line-height: 1.1 !important;
            letter-spacing: -1px !important;
        }

        h2 {
            font-size: 2.2rem !important;
            font-weight: 750 !important;
            line-height: 1.1 !important;
        }

        h3 {
            font-size: 1.5rem !important;
            font-weight: 700 !important;
        }


        /* =========================
           NORMAL TEXT
           ========================= */

        p {
            font-weight: 450;
            line-height: 1.5;
        }


        /* =========================
           PRIMARY BUTTON
           ========================= */

        button {

            border-radius: 0.9rem !important;

            background:
                linear-gradient(
                    135deg,
                    #2563EB,
                    #4F46E5
                ) !important;

            color: white !important;

            padding: 10px 22px !important;

            border: 1px solid rgba(255,255,255,0.12) !important;

            font-family: 'Outfit', sans-serif !important;

            font-weight: 650 !important;

            box-shadow:
                0 8px 20px rgba(37, 99, 235, 0.25) !important;

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease !important;
        }


        /* =========================
           SECONDARY BUTTON
           ========================= */

        button[kind="secondary"] {

            border-radius: 0.9rem !important;

            background:
                linear-gradient(
                    135deg,
                    #6366F1,
                    #7C3AED
                ) !important;

            color: white !important;

            padding: 10px 22px !important;

            border: none !important;

            font-weight: 650 !important;

            box-shadow:
                0 8px 20px rgba(99, 102, 241, 0.25) !important;
        }


        /* =========================
           TERTIARY BUTTON
           ========================= */

        button[kind="tertiary"] {

            border-radius: 0.9rem !important;

            background: #111827 !important;

            color: white !important;

            padding: 10px 22px !important;

            border: none !important;

            font-weight: 650 !important;
        }


        /* =========================
           BUTTON HOVER
           ========================= */

        button:hover {

            transform: translateY(-2px) scale(1.02) !important;

            box-shadow:
                0 12px 28px rgba(0, 0, 0, 0.20) !important;
        }


        /* =========================
           INPUT BOXES
           ========================= */

        input,
        textarea {

            border-radius: 0.8rem !important;

            border: 1px solid #CBD5E1 !important;
        }


        /* =========================
           STREAMLIT ALERTS
           ========================= */

        [data-testid="stAlert"] {

            border-radius: 0.9rem !important;
        }

        </style>
    """, unsafe_allow_html=True)