import streamlit as st
import pandas as pd
import numpy as np

def projectsatu():
    data = pd.read_excel('data_rfm.xlsx')

    st.title("Customer Segmentation Superstore")

    st.subheader('Yearly Sales Trend',divider=True)
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['year_order_date'] = data['order_date'].dt.year

    data_group = data.groupby(['year_order_date', 'category'])['sales'].sum().reset_index()

    pivot_df = data_group.pivot_table(index='year_order_date', columns='category', values='sales', aggfunc='sum', fill_value=0)
    pivot_df.index = pivot_df.index.astype(str)

    st.line_chart(pivot_df)

    if "visible" not in st.session_state:
        st.session_state.visible = "visible"
        st.session_state.disabled = False
        st.session_state.horizontal = False
            
    eval_produk = st.radio(
        "Evaluasi Produk",
        ["Furniture", "Office Supplies", "Technology"],
        key="visibility",
        label_visibility=st.session_state.visible,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
        )

    if eval_produk == "Furniture":
        import furniture
        furniture.furniture()
    elif eval_produk == "Office Supplies":
        import officesupplies
        officesupplies.office_supplies()
    elif eval_produk == "Technology":
        import technology
        technology.technology()


    



