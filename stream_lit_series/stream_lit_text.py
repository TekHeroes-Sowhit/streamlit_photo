
import streamlit as st
import pandas as pd
label=pd.DataFrame("Column1":[1,2,3,4,5],"column2":[11,12,13,14,15])
st.title('Hello')
st.subheader('Hi,I am your subheader')
st.text("I am a text function and programmers")
st.markdown("**Hello** world")

st.markdown("---")

st.markdown("[Google](https://www.google.com)")
st.caption("Hello")
st.latex(r"\begin{pmatrix}a&b\\c&d\end") ## For the mathematical functions
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)
code="""
print(Hello)
def func():
    return 0;
"""

st.code(code,language="python")

st.write("## H2")

st.metric(label="Wind speed", value="120ms\^-1",delta="1.4ms\^-1")

st.table(label)
## Extension Fast unicode Math connector

st.dataframe(table)

## Image
st.image('Image.jpg',caption="This is my image",width="680")
st.audio("audio.mp3")
st.video("Video.mp4")



