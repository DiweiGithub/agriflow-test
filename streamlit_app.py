import streamlit as st

import yaml
from yaml.loader import SafeLoader

import pandas as pd
from PIL import Image

import streamlit_authenticator as stauth


st.set_page_config(initial_sidebar_state="collapsed")

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



img=Image.open('images/logo.PNG')
st.image(img)
#st.logo("images/logo.PNG", icon_image="images/logo.PNG")

st.sidebar.markdown("Hi!")
    
st.subheader( "Empowering Farmers, Nurturing Growth")

with open('data/Admin.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

st.markdown("Your care will shape **the future of agriculture** in Europe!")

st.header( '''Welcome to :green[AgriFlow]!''', divider='rainbow')
st.markdown ( ''' :green[AgriFlow]is **really** ***cool*** !!! :sunglasses:''' )

with open('data/Admin.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized'])

#st.header( '''Welcome to :green[AgriFlow]!''', divider='rainbow')

authenticator.login('main', fields = {'Form name': 'Login'})
if st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
elif st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')        
    st.switch_page("pages/1_🏠_Homepage.py")    

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
    signup = st.button("Sign up")
    reset=st.button("Reset Password")
    forget=st.button("Forget Password")
    if signup:
        st.switch_page("pages/reset.py")   


#st.divider()
