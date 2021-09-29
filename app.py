import fantasy
import rushing
import streamlit as st
import utils

###### Initialization ######
st.set_page_config(  # Alternate names: setup_page, page, layout
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
	page_title="NFL Data Application",  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)

# Initialize session state variables
utils.initializeSession()

PAGES = {
    "Fantasy Center": fantasy,
    "Rushing Stats": rushing
}

# Configure navigation pane
st.sidebar.title('Navigation')
selection = st.sidebar.radio("View:", list(PAGES.keys()))
page = PAGES[selection]
page.app()

# add year selection
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990,2021 + 1))), key='year')

col1, col2 = st.beta_columns(2)

col2.markdown("""
**Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")