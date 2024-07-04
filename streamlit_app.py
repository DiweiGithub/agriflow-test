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
        #Creating a new user registration widget
        try:
            email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
            if email_of_registered_user:
                with open('data/Admin.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.success('User registered successfully')
        except Exception as e:
        st.error(e)

'''

    if st.session_state["name"] is None:
        #st.warning('Please sign up')
        if signup:  
            #Creating a new user registration widget
            try:
                email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
                if email_of_registered_user:
                    with open('data/Admin.yaml', 'w') as file:
                        yaml.dump(Admin, file, default_flow_style=False)
                    st.success('User registered successfully')
            except Exception as e:
                st.error(e)
    
        elif reset:
            try:
                if authenticator.reset_password(st.session_state["username"]):
                    submitted = st.form_submit_button("Submit")
                    st.success('Password modified successfully')
            except Exception as e:
                st.error(e)
        elif forget:
            try:
                username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
                if username_of_forgotten_password:
                    st.success('New password to be sent securely')
                    # The developer should securely transfer the new password to the user.
                elif username_of_forgotten_password == False:
                    st.error('Username not found')
            except Exception as e:
                st.error(e)
'''
#st.divider()
