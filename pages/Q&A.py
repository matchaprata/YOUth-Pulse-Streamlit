import streamlit as st
from datetime import datetime
# Custom Filter

def createSection(section):
    st.subheader(f'{section}', divider='red')


st.title('Q&A')
# This static filter
tab1, tab2, tab3, tab4 = st.tabs(["Index", "Education", "Environment", f"Budget{datetime.today().year}"])
with tab1:
    allHeader = ['Recently Answered', 'Most Interesting']
    for header in allHeader:
        createSection(header)
with tab2:
    allHeader = []
    createSection("1")
with tab3:
    allHeader = []
    createSection("2")
with tab4:
    allHeader = []
    createSection("3")
