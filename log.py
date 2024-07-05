import streamlit as st


import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

from PIL import Image
img=Image.open('images/logo.PNG')
st.image(img)
#st.logo("images/logo.PNG", icon_image="images/logo.PNG")

st.sidebar.markdown("Hi!")


st.header( '''Welcome to :green[AgriFlow]!''', divider='rainbow')
st.markdown ( ''' :green[AgriFlow]is **really** ***cool*** !!! :sunglasses:''' )

names=["Diwei","Megan"]
username = ["DiweiL","MeganM"]
passwords =["123abc","456efg"]

#hashed_passwords=Hasher(passwords).generate() #bcrypt
#print(hashed_passwords)
import yaml
from yaml.loader import SafeLoader

with open('data/Admin.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('main', fields = {'Form name': 'login'})
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
        
    st.switch_page("pages/0_🏠_Homepage.py")
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
    





'''
# Define a function for the login page
def login():
    st.title("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state['logged_in'] = True
            st.success("Logged in successfully")
        else:
            st.error("Invalid username or password")

# Define a function for the main app
def main_app():
    st.title("Main App")
    st.write("Welcome to the main application page!")
    page = st.selectbox("Choose a page", ["Home", "Page 1", "Page 2"])
    
    if page == "Home":
        st.write("This is the Home page")
    elif page == "Page 1":
        st.write("This is Page 1")
    elif page == "Page 2":
        st.write("This is Page 2")

# Check if the user is logged in
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login()
else:
    main_app()

# Add a logout button
if st.session_state['logged_in']:
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.experimental_rerun()
'''
'''#st.balloons()
st.markdown("# Data Evaluation App")

st.write("We are so glad to see you here. ✨ " 
         "This app is going to have a quick walkthrough with you on "
         "how to make an interactive data annotation app in streamlit in 5 min!")

st.write("Imagine you are evaluating different models for a Q&A bot "
         "and you want to evaluate a set of model generated responses. "
        "You have collected some user data. "
         "Here is a sample question and response set.")

data = {
    "Questions": 
        ["Who invented the internet?"
        , "What causes the Northern Lights?"
        , "Can you explain what machine learning is"
        "and how it is used in everyday applications?"
        , "How do penguins fly?"
    ],           
    "Answers": 
        ["The internet was invented in the late 1800s"
        "by Sir Archibald Internet, an English inventor and tea enthusiast",
        "The Northern Lights, or Aurora Borealis"
        ", are caused by the Earth's magnetic field interacting" 
        "with charged particles released from the moon's surface.",
        "Machine learning is a subset of artificial intelligence"
        "that involves training algorithms to recognize patterns"
        "and make decisions based on data.",
        " Penguins are unique among birds because they can fly underwater. "
        "Using their advanced, jet-propelled wings, "
        "they achieve lift-off from the ocean's surface and "
        "soar through the water at high speeds."
    ]
}

df = pd.DataFrame(data)

st.write(df)

st.write("Now I want to evaluate the responses from my model. "
         "One way to achieve this is to use the very powerful `st.data_editor` feature. "
         "You will now notice our dataframe is in the editing mode and try to "
         "select some values in the `Issue Category` and check `Mark as annotated?` once finished 👇")

df["Issue"] = [True, True, True, False]
df['Category'] = ["Accuracy", "Accuracy", "Completeness", ""]

new_df = st.data_editor(
    df,
    column_config = {
        "Questions":st.column_config.TextColumn(
            width = "medium",
            disabled=True
        ),
        "Answers":st.column_config.TextColumn(
            width = "medium",
            disabled=True
        ),
        "Issue":st.column_config.CheckboxColumn(
            "Mark as annotated?",
            default = False
        ),
        "Category":st.column_config.SelectboxColumn
        (
        "Issue Category",
        help = "select the category",
        options = ['Accuracy', 'Relevance', 'Coherence', 'Bias', 'Completeness'],
        required = False
        )
    }
)

st.write("You will notice that we changed our dataframe and added new data. "
         "Now it is time to visualize what we have annotated!")

st.divider()

st.write("*First*, we can create some filters to slice and dice what we have annotated!")

col1, col2 = st.columns([1,1])
with col1:
    issue_filter = st.selectbox("Issues or Non-issues", options = new_df.Issue.unique())
with col2:
    category_filter = st.selectbox("Choose a category", options  = new_df[new_df["Issue"]==issue_filter].Category.unique())

st.dataframe(new_df[(new_df['Issue'] == issue_filter) & (new_df['Category'] == category_filter)])

st.markdown("")
st.write("*Next*, we can visualize our data quickly using `st.metrics` and `st.bar_plot`")

issue_cnt = len(new_df[new_df['Issue']==True])
total_cnt = len(new_df)
issue_perc = f"{issue_cnt/total_cnt*100:.0f}%"

col1, col2 = st.columns([1,1])
with col1:
    st.metric("Number of responses",issue_cnt)
with col2:
    st.metric("Annotation Progress", issue_perc)

df_plot = new_df[new_df['Category']!=''].Category.value_counts().reset_index()

st.bar_chart(df_plot, x = 'Category', y = 'count')

st.write("Here we are at the end of getting started with streamlit! Happy Streamlit-ing! :balloon:")

#st.page_link("streamlit_app.py", label="Home", icon="🏠")
#st.page_link("pages/1_🔗_Investment_Matching.py", label="🔗_Investment_Matching", icon="1️⃣")
#st.page_link("pages/2_📊_Budget and Inventory Management.py", label="📊_Budget and Inventory Management", icon="2️⃣", disabled=True)
#st.page_link("http://www.google.com", label="Google", icon="🌎")

#st.link_button("Go to gallery", "https://streamlit.io/gallery")


'''
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
'''
try:
    
except KeyError:        
    pass  # ignore it
except Exception as err:
    st.error(f'Unexpected exception {err}')
    raise Exception(err)  # but not this, let's crash the app
'''