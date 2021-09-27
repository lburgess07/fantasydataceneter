import fantasy
import rushing
import streamlit as st

###### Initialization ######
st.set_page_config(  # Alternate names: setup_page, page, layout
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
	page_title="NFL Data Application",  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)

# Configure view options session state
if 'num_items' not in st.session_state:
    st.session_state['num_items'] = 10 #default to 10
if 'year' not in st.session_state:
    st.session_state['year'] = 2021

PAGES = {
    "Fantasy": fantasy,
    "Rushing": rushing
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990,2021 + 1))), key='year')

col1, col2 = st.beta_columns(2)

numItemsOptions = [5, 10, 20, 50, 100, 500, 1000]
#col1.slider("# of Entries:", min_value=1, max_value=200, step=5, key='num_items')
col1.selectbox('# of Entries', numItemsOptions, key='num_items')
#st.session_state.num_items = col1.selectbox('# Displayed Entries', numItemsOptions)
#col1.number_input(label='num items', key='num_items' )


col2.markdown("""
**Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")