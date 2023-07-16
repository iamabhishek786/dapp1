import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px         # order does not matter here! (1-4)

# loading the data
@st.cache_data
def load_data():
    path = 'data/kc_house_data.csv'
    df = pd.read_csv(path)
    return df

# call the load_data function
with st.spinner('Loading the data'):
    df=load_data()

# create a title for your app
st.title('House Price Data Analysis')
st.subheader('Key Performance Indicator')

# to get the list of all colummns
cols = df.columns.tolist()
selected_cols = st.multiselect('Select columns', cols)
st.write(f'You Selected: {len(selected_cols)} columns')

for col in selected_cols:
    st.subheader(f'Column: {col}')
    try:
        st.metric(label=f'Mean {col}',
                  value = round(df[col].mean()),
                  delta = round(df[col].std()))
        st.line_chart(df[col], use_container_width = True)
    except:
        st.error(f'Cannot display {col} numeric data')


