import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# import snowflake.connector
# import streamlit_option_menu
# from streamlit_option_menu import option_menu

price_df = pd.read_csv('wfp_food_prices_hti.csv', header=0,  skiprows=[1,])
current_data = price_df.sort_values(by=['date'])
all_departement = ['all'] + list(price_df['admin1'].unique())
all_market = ['all'] + list(price_df['market'].unique())
all_prince = ['HTG', 'USD']

disable = False
with st.sidebar:
    d_option = st.selectbox(
        "Choose a department",
        tuple(all_departement),
    )
    if d_option == 'all':
        disable = True
    else:
        disable = False
        select_department = price_df[price_df['admin1'] == d_option]
        current_data = select_department.sort_values(by=['date'])
        select_market_df = select_department['market'].unique()
        all_market = select_market_df

    m_option = st.selectbox(
        "Choose a market",
        tuple(all_market),
        disabled=disable
    )


if d_option in all_departement:
    st.header('Haiti Food price...')
    # Create a row layout
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

    with st.container():
        c1.write("c1")
        c2.write("c2")

    with st.container():
        c3.write("c3")
        c4.write("c4")

    with c1:
        mais_data = current_data[current_data['commodity']
                                 == 'Maize meal (local)']
        c_fig = px.line(mais_data, x='date', y="price",
                        title='Maize meal (local)')
        st.plotly_chart(c_fig)

    with c2:
        rice_data = current_data[current_data['commodity']
                                 == 'Rice (tchako)']
        r_fig = px.line(rice_data, x='date', y="price",
                        title='Rice (tchako)')
        st.plotly_chart(r_fig)

    with c3:
        wheat_data = current_data[current_data['commodity']
                                  == 'Wheat flour (imported)']
        w_fig = px.line(wheat_data, x='date', y="price",
                        title='Wheat flour (imported)')
        st.plotly_chart(w_fig)

    with c4:
        m_i_data = current_data[current_data['commodity']
                                == 'Maize meal (imported)']
        mi_fig = px.line(m_i_data, x='date', y="price",
                         title='Maize meal (imported)')
        st.plotly_chart(mi_fig)

# fig_m = px.line(malaria_df, x='YEAR (DISPLAY)', y="Numeric", title=m_title)
