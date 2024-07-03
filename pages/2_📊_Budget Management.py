import streamlit as st
import numpy as np
import pandas as pd
import altair as alt



# Page title
st.set_page_config(page_title='Budget Management', page_icon='📊',initial_sidebar_state="collapsed")
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
st.title('📊 AgriFlow - Budget Management')

st.divider()



with st.expander('About this app'):
  st.markdown('**What can this app do?**')
  st.info('This app shows Budget Management.')
  st.markdown('**How to use the app?**')
  st.warning('To engage with the app, 1. Select expense of your interest in the drop-down selection box and then 2. Select the year duration from the slider widget. As a result, this should generate an updated editable DataFrame and line plot.')

st.subheader('Where does my money go? ')

# Load data
df = pd.read_csv('data/expenditures_summary.csv')
df.year = df.year.astype('int')


# Input widgets
## Genres selection
expen_list = df.expenditure.unique()
expen_selection = st.multiselect('Select expenditure', expen_list, ['Seeds', 'equipments','Labor', 'Pesticides and Herbicidesation', 'Financing Costs'])

## Year selection
year_list = df.year.unique()
year_selection = st.slider('Select year duration', 1986, 2006, (2000, 2016))
year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

df_selection = df[df.expenditure.isin(expen_selection) & df['year'].isin(year_selection_list)]
reshaped_df = df_selection.pivot_table(index='expenditure', columns='year', values='euro', aggfunc='sum', fill_value=0)
reshaped_df = reshaped_df.sort_values(by='expenditure', ascending=False)


# display the dataframe and highlight the max
st.dataframe(reshaped_df.style.highlight_max(axis=0))
#display the dataframe with modification option
df_editor = st.data_editor(reshaped_df, height=None, use_container_width=True,
                            column_config={"expenditure": st.column_config.TextColumn("expenditure")},
                            num_rows="dynamic")
df_chart = pd.melt(df_editor.reset_index(), id_vars='expenditure', var_name='year', value_name='euro')

# Display chart
chart = alt.Chart(df_chart).mark_line().encode(
            x=alt.X('year:N', title='Year'),
            y=alt.Y('euro:Q', title='Euro ($)'),
            color='expenditure:N'
            ).properties(height=320)
st.altair_chart(chart, use_container_width=True)
df_total=pd.pivot_table(df,index='year',values='euro',aggfunc=np.sum).reset_index()
# display the dataframe and highlight the max
st.dataframe(df_total.style.highlight_max(axis=0))
st.bar_chart(df_total, x = 'year', y = 'euro')
