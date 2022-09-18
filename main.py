import streamlit as st
import subprocess

st.header('🎈 R x Python Streamlit App')

st.sidebar.markdown('''
# About
This demo shows the use of R in a Streamlit App by showcasing 3 example use cases.
The R code for all 3 examples are rendered on-the-fly in this app.
R packages used:
- `ggplot2`
- `cowplot`
''')

st.subheader('1. Printing text in R')
with st.expander('See code'):
  code1 = '''print("Hello world ...")
  '''
  st.code(code1, language='R')
process1 = subprocess.Popen(["Rscript", "hello.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)


process2 = subprocess.Popen(["Rscript", "fetch_datasus.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


if st.button('Extrair dados'):
  result2 = process2.communicate()
  st.write(result2)
