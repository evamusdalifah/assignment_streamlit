import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data

def technology():
    data = pd.read_excel('data_rfm.xlsx')

    st.subheader('Customer Segmentation of Technology',divider=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    data_tech = data[data['category'] == 'Technology']
    st.write('By Subcategory')
    st.bar_chart(data_tech, x="segment", y="sales", color="subcategory", horizontal=True)

    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('By Region')
    st.bar_chart(data_tech, x="segment", y="sales", color="region", horizontal=True)