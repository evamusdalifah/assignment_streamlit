import streamlit as st
import pandas as pd
import numpy as np

def projectsatu():
    data = pd.read_excel('data_rfm.xlsx')

    data['order_date'] = pd.to_datetime(data['order_date'])
    data = data.sort_values('order_date')
    data = data.set_index('order_date')

    data["month_order"] = data["order_date"].dt.month
    data["year_order"] = data["order_date"].dt.year
    data['new_order_date'] = data['month_order'] + '-' + data['year_order']

    sales_per_month = data.groupby('new_order_date')['sales'].sum()

    st.line_chart(data=data, x='new_order_date', y='sales_per_month')