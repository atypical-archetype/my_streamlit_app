import streamlit as st

st.title("Code project app")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your variety of operation")

variable1 = st.selectbox("your fav option: ",["fast api","Django","Flask","Js"])


