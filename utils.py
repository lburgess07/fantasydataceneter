from pandas.core.frame import DataFrame
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

@st.cache
def load_data(stat_type, year, dtype = str):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/" + stat_type + ".htm"
    html = pd.read_html(url, header = 1)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
    raw = raw.fillna('')
    # Drop 'RK' column
    playerstats = raw.drop(['Rk'], axis=1).astype(dtype=dtype) 
    # Make Pos uppercase
    header = playerstats.head(0)
    if ('FantPos' in header):
        playerstats.FantPos = playerstats.FantPos.str.upper()
    elif ('Pos' in header):
        playerstats.Pos = playerstats.Pos.str.upper()
    
    return playerstats

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strs <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Export to CSV</a>'
    return href

def compose_heatmap(df):
    import os
    st.header('Intercorrelation Matrix Heatmap')
    df.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot(f)
    os.remove('output.csv')

#@st.cache
def rowsToHeight(rows:int):
    return int(rows * 28) # each row is 30 px