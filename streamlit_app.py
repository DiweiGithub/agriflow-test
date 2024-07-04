import streamlit as st
from PIL import Image

import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

import streamlit as st 
import pandas as pd
from PIL import Image
import yaml

import streamlit_authenticator as stauth
from yaml.loader import SafeLoader


st.set_page_config(initial_sidebar_state="collapsed")
'''
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)'''



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

logout= authenticator.logout()
#st.header( '''Welcome to :green[AgriFlow]!''', divider='rainbow')

col1, col2, col3 = st.columns(3)
with col1:
    match = st.button("🧦 Investment Matching")
with col2:
    management = st.button("📊 Budget Management")
with col3:
    prediction = st.button("📈 Predictive Trend Analytics")
#st.divider()
if match:
    st.write("You have selected 🧦 Investment Matching")
    st.switch_page("pages/3_🔗_Investment_Matching.py")
elif management:
    st.write("You have selected 📊 Budget Management")
    st.switch_page("pages/2_📊_Budget Management.py")
elif prediction:
    st.write("You have selected 📈 Predictive Trend Analytics")
    st.switch_page("pages/4_📈_Predictive_Trend_analytics.py")

name, authentication_status, username = authenticator.login('main', fields = {'Form name': 'login'})
print(name, authentication_status, username)
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')        
    st.switch_page("pages/1_🏠_Homepage.py")    

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif name == None:
    st.warning('Please sign up')
    st.button("Sign up")
elif authentication_status == None:
    st.warning('Please enter your username and password')

#st.divider()
