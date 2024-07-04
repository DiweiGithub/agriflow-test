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

#st.header( '''Welcome to :green[AgriFlow]!''', divider='rainbow')
'''
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
'''
authenticator.login('main', fields = {'Form name': 'login'})
if st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')        
    st.switch_page("pages/1_🏠_Homepage.py")    

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
    if st.session_state["name"] is None:
        #st.warning('Please sign up')
        if st.button("Sign up"):  
            #Creating a new user registration widget
            try:
                email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
                if email_of_registered_user:
                    with open('data/Admin.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
                    st.success('User registered successfully')
            except Exception as e:
                st.error(e)
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

#st.divider()
