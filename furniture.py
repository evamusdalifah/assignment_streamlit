import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data

def furniture():
    data = pd.read_excel('data_rfm.xlsx')

    st.subheader('Customer Segmentation of Furniture',divider=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    data_furniture = data[data['category'] == 'Furniture']
    st.write('By Subcategory')
    st.bar_chart(data_furniture, x="segment", y="sales", color="subcategory", horizontal=True)

    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('By Region')
    st.bar_chart(data_furniture, x="segment", y="sales", color="region", horizontal=True)




