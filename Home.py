import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/pic.png")

with col2:
    st.title("Vivek Chandra")
    content = """
    As an engineer with an MBA, I am skilled in both technical analysis and business strategy. 
    I am able to use my strong foundation in data and analytics to drive informed decision-making 
    and add value to any organization. With experience in both business and technical fields, 
    I am able to bridge the gap between the two and effectively communicate complex ideas to both technical 
    and non-technical audiences.    
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

df = pandas.read_csv("data.csv", sep=";")

col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
