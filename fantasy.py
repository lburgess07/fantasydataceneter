from pandas.core.frame import DataFrame
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import utils

def app():
    num_items = st.session_state.num_items
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title('NFL Fantasy Stats')

    st.sidebar.header('Selections')
    #selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990,2021 + 1))))

    # dtype = { 
    # 'Player':'str',
    # 'Tm':'str',
    # 'Age':'int',
    # 'Pos':'str',
    # 'G':'int',
    # 'GS':'int',
    # 'Att':'int',
    # 'Yds':'int',
    # '1D':'int',
    # 'Lng':'int',
    # 'Y/A':'float',
    # 'Y/G':'float',
    # 'Fmb':'int'
    # }
    #     return playerstats
    #playerstats = utils.load_data("fantasy", selected_year)
    playerstats = utils.load_data("fantasy", st.session_state.year)
    # Sidebar - Team selection
    sorted_unique_team = sorted(playerstats.Tm.unique())
    selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

    # Sidebar - Position selection
    sorted_unique_pos = sorted(playerstats.FantPos.unique())
    selected_pos = st.sidebar.multiselect('Position', sorted_unique_pos, sorted_unique_pos)

    # Filtering data
    df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.FantPos.isin(selected_pos))]
    # Reset index after sorting
    #df_selected_team = df_selected_team.reset_index(0, drop= True)

    out = st.dataframe(df_selected_team, height=utils.rowsToHeight(num_items))

    st.markdown(utils.filedownload(df_selected_team), unsafe_allow_html=True)

    # Heatmap
    if st.button('Intercorrelation Heatmap'):
        utils.compose_heatmap(df_selected_team)
    
    numItemsOptions = [5, 10, 20, 50, 100, 500, 1000]
    col1.selectbox('# of Entries', numItemsOptions, key='num_items')