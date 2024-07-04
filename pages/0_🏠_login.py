import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher
import yaml
from yaml.loader import SafeLoader
from PIL import Image

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
)
'''

img=Image.open('images/logo.PNG')
st.image(img)
#st.logo("images/logo.PNG", icon_image="images/logo.PNG")

st.sidebar.markdown("Hi!")
    
st.subheader( "Empowering Farmers, Nurturing Growth")

st.markdown("Your care will shape **the future of agriculture** in Europe!")

st.header( '''Welcome to :green[AgriFlow]!''', divider='rainbow')
st.markdown ( ''' :green[AgriFlow] is **really** ***cool*** !!! :sunglasses:''' )

names=["Diwei","Megan"]
username = ["DiweiL","MeganM"]
passwords =["123abc","456efg"]

#hashed_passwords=Hasher(passwords).generate() #bcrypt
#print(hashed_passwords)

with open('data/Admin.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)
authenticator.login('main', fields = {'Form name': 'Login'})
if st.session_state["authentication_status"]:
    #authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')        
    st.switch_page("pages/1_🏠_Homepage.py")
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
elif st.session_state["name"] == None:
    st.warning('Please sign up')
    st.button("Sign up")
authenticator.logout()

if st.session_state["authentication_status"]:
    try:
        if authenticator.reset_password(st.session_state["username"]):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)
#Creating a new user registration widget
try:
    email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
    if email_of_registered_user:
        with open('data/Admin.yaml', 'w') as file:
            yaml.dump(Admin, file, default_flow_style=False)
        st.success('User registered successfully')
except Exception as e:
    st.error(e)
#Creating a forgot password widget
try:
    username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
    if username_of_forgotten_password:
        st.success('New password to be sent securely')
        # The developer should securely transfer the new password to the user.
    elif username_of_forgotten_password == False:
        st.error('Username not found')
        #Creating a forgot username widget
        try:
            username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
            if username_of_forgotten_username:
                st.success('Username to be sent securely')
                # The developer should securely transfer the username to the user.
            elif username_of_forgotten_username == False:
                st.error('Email not found')
        except Exception as e:
            st.error(e)
except Exception as e:
    st.error(e)






