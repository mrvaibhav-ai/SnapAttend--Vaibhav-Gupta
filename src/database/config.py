import streamlit as st
from supabase import create_client, Client


SUPABASE_URL = st.secrets["https://ckqlpzycpciurhrukxmd.supabase.co"]
SUPABASE_KEY = st.secrets["sb_publishable_yu2qu3IhyQx5J5sM2ElsdA_BJ2GvUAY"]


supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)