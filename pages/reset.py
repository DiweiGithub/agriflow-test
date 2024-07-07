
import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader
import time

with open('data/Admin.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized'])

try:
    email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
    if email_of_registered_user:
        with open('data/Admin.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
        st.success('User registered successfully')

        if "photo" not in st.session_state:
            st.session_state["photo"]="not done"
        def change_photo_state():
            st.session_state["photo"] =='done'
        uploaded_photo = st.file_uploader("Upload a photo",on_change=change_photo_state)
        camera_photo = st.camera_input("Take a photo",on_change=change_photo_state)
        if st.session_state["photo"] =="done":
            progress_bar = st.progress(0)
            for perc_completed in range(100):
                time.sleep(0.05)
                progress_bar.progress(perc_completed+1)
            if uploaded_photo is None:
                st.image(camera_photo)
            else:
                st.image(uploaded_photo)
        #st.switch_page("streamlit_app.py")   
except Exception as e:
    st.error(e)
