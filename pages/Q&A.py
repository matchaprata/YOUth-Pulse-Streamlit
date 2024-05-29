import streamlit as st
import json as json

file = open('./data/qa.json')
qa_data = json.load(file)

# Custom Filter

def createSection(section):
    st.subheader(f'{section}', divider='red')

def createContent(index):
    createSection(qa_data['answered'][index]['section_title'])
    for section in qa_data['answered'][index]['q']:
        tempContainer = st.container(height=0, border=True)
        with tempContainer:
            st.write(section['content']['question'])
            st.write(section['content']['answer'])


st.title('Q&A')
# This static filter
tab1, tab2, tab3, tab4 = st.tabs(["Index", "Education", "Environment", f"Budget2024"])
with tab1:
    allHeader = ['Recently Answered', 'Most Interesting']
    for header in allHeader:
        createSection(header)
        if header == 'Recently Answered':
            for section in qa_data['answered']:
                latest_id = int(10 * (section['latest'] - section['id']))
                try:
                    latest_content = section['q'][latest_id-1]['content']
                    tempContainer = st.container(height=0, border=True)
                    with tempContainer:
                        st.write(latest_content['question'])
                        st.write(latest_content['answer'])
                except:
                    print(latest_id)
                    print(section)
                    print("Index Error")
        elif header == 'Most Interesting':
            tempContainer = st.container(height=0, border=True)
            with tempContainer:
                st.caption("94 people asked this question.")
                st.write("Q: Where does my money go?")
                st.write("A: 20% of your income contributes to your CPF account, leaving you with 80% of your income to spend on")


with tab2:
    createContent(0)

with tab3:
    createContent(1)

with tab4:
    createContent(2)

