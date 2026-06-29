import streamlit as st

st.set_page_config(
     page_title='Happy Birthday',
     page_icon='Babe.png'
)

st.title("Happy Birthday Zarnab")

if st.button("Click me"):
    st.audio('HBDS.mp3')
    st.image('BluF.png')
    st.success("Happy")
    st.warning("Birthday")
    st.error("Zarnab")
    st.image('RdF.png')
    st.balloons()
    st.balloons()
    st.balloons()
    st.subheader(f"Happy birthday Zarnab")
    st.image('VaitF.png')
    st.image('YeloF.png')

if st.button("???"):
    st.image('HBS.png')
    for i in range(1,10):
            st.balloons()
