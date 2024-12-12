import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

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