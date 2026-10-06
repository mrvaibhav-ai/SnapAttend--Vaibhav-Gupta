import streamlit as st


from supabase import create_client, Client

supabase: Client = create_client(
    st.secrets["https://ckqlpzycpciurhrukxmd.supabase.co"],
    st.secrets["sb_publishable_yu2qu3IhyQx5J5sM2ElsdA_BJ2GvUAY"]
)