import streamlit as st
import numpy as np


# Page title
st.set_page_config(page_title='Predictive Trend Analytics', page_icon='📈',initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
home_page_button= st.button("Home Page")
if home_page_button:
  st.switch_page("pages/1_🏠_Homepage.py")
st.divider()
st.header("Welcome!")
st.header("This page is available to all members.")
st.title('📈 AgriFlow - Predictive Trend Analytics')

st.divider()

with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app will provide you Trend Analytics.')
  st.markdown('**How to use the app?**')
  st.warning('I need to think about it.')

st.subheader('How am I prepared for the future? ')

df = st.session_state