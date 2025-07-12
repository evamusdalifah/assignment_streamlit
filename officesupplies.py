import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data

def office_supplies():
    data = pd.read_excel('data_rfm.xlsx')

    st.subheader('Customer Segmentation of Office Supplies',divider=True)
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    data_of = data[data['category'] == 'Office Supplies']
    st.write('By Subcategory')
    st.bar_chart(data_of, x="segment", y="sales", color="subcategory", horizontal=True)

    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('By Region')
    st.bar_chart(data_of, x="segment", y="sales", color="region", horizontal=True)