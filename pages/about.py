import streamlit as st

#create a title for your app
st.title('House Price Data analysis')
st.subheader('About this App')

st.markdown("""
This app performs simple data analysis on the ***House Price*** dataset.
* **Python libraries:**
    - pandas
    - streamlit
    - numpy
    - matplotlib
    - seaborn
* **Data source:** [Kaggle](https://www.kaggle.com/datasets/amarnadhreddyavuduri/kc-house-dataset)
<img src= "https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1000">
""", unsafe_allow_html=True)
