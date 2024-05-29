import streamlit as st
from datetime import datetime
import json as json

file = open('./data/qa.json')
qa_data = json.load(file)

# Custom Filter

def createSection(section):
    st.subheader(f'{section}', divider='red')


st.title('Q&A')
# This static filter
tab1, tab2, tab3, tab4 = st.tabs(["Index", "Education", "Environment", f"Budget {datetime.today().year}"])
with tab1:
    allHeader = ['Recently Answered', 'Most Interesting']
    for header in allHeader:
        createSection(header)
        if header == 'Recently Answered':
            for sections in qa_data['answered']:
                latest_id = int(10 * (sections['latest'] - sections['id']))
                try:
                    latest_content = sections['q'][latest_id]['content']
                    tempContainer = st.container(height=0, border=True)
                    with tempContainer:
                        st.write(latest_content['question'])
                        st.write(latest_content['answer'])
                except:
                    print(latest_id)
                    print(len(qa_data['answered']))
                    print("Send a+error to Admin")
        elif header == 'Most Interesting':


with tab2:
    allHeader = []
    createSection("1")
with tab3:
    allHeader = []
    createSection("2")
with tab4:
    allHeader = []
    createSection("3")
