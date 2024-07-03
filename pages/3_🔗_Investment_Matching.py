import streamlit as st
import pandas as pd
from datetime import date
import datetime
import numpy as np
from PIL import Image


# Page title
st.set_page_config(page_title='Investment Matching', page_icon='🧦',initial_sidebar_state="collapsed")
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
st.header("This page is available to all public.")
st.title('🧦 AgriFlow - Investment Matching')

st.divider()



with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app will match the investors and farmers.')
  st.markdown('**How to use the app?**')
  st.warning('I need to think about it.')


# Load data
df = pd.read_csv('data/matching_data.csv')

#df_offer=df[df['amount_to_offer'].notnull()].copy()
#df_offer.drop(columns={'amount_to_seek'},inplace=True)
#df_offer.amount_to_offer= df_offer.amount_to_offer.astype('float')

#df_seek=df[df['amount_to_seek'].notnull()].copy()
#df_seek.drop(columns={'amount_to_offer'},inplace=True)
#df_seek.amount_to_seek = df_seek.amount_to_seek.astype('float')
#df_all = df_offer.merge(df_seek,how='outer',on='Interest',suffixes=('_offer','_seek'))

df_seek = pd.read_csv('data/farmer_data.csv')
df_seek.amount_to_seek= df_seek.amount_to_seek.astype('float')
df_seek["date"] = pd.to_datetime(df_seek["date"],format="%d/%m/%Y")
df_seek['date'] = df_seek['date'].dt.date
df_seek.drop(columns={'no'},inplace=True)
df_offer = pd.read_csv('data/Investor_data.csv')
df_offer.amount_to_offer= df_offer.amount_to_offer.astype('float')
df_offer["date"] = pd.to_datetime(df_offer["date"],format="%d/%m/%Y")
df_offer['date'] = df_offer['date'].dt.date
df_offer.drop(columns={'no'},inplace=True)


df_all = df_offer.merge(df_seek,how='outer',
                        on='Interest',suffixes=('_offer','_seek')
)
col1, col2 =st.columns(2)
with col1:
   st.write("The gap in amount")
   option = st.selectbox("Select the diff in amount",    
                         (500,1000,2000,5000,10000,50000,100000,500000))
   st.write("You selected:", option)
with col2:
   st.write("The date")
   data_selection = st.slider('Select the data range', datetime.date(2019, 7, 6), date.today(), (datetime.date(date.today().year-1, date.today().month, 1), date.today()))
   #data_selection_list=list(np.arange(data_selection[0], data_selection[1]))
   st.write("You selected the date starting from :", data_selection[0])
   st.write("You selected the date ends to :", data_selection[1])
   

#amt_selection = st.slider('Select the diff in amount', 500, 5000, (1000, 5000))
df_match=df_all[(abs(df_all['amount_to_offer'].fillna(0)-df_all['amount_to_seek'].fillna(0))< option)
                &df_all['amount_to_offer'].notnull()
                &df_all['amount_to_seek'].notnull()
                &(df_all['date_offer']<data_selection[1])
                  &(df_all['date_offer']>data_selection[0])].copy()

st.metric(label="Matches", value=df_match.shape[0])

# Display DataFrame

df_editor = st.data_editor(df_match,height=212, use_container_width=True,
                            column_config={"Interest": st.column_config.TextColumn("Interest")},
                            num_rows="dynamic")



