import streamlit as st
import pandas as pd
import numpy as np

##Title of teh application
st.title("Hello Streamlit!!!")

##Display simple test
st.write("Thsi is a simple text")

##Create a simple DataFrame
df = pd.DataFrame({
    'First Column': [1, 2, 3, 4],
    'Second Column': [10, 20, 30, 40]
})

##Display the DataFrame
st.write("Here is teh DataFrame")
st.write(df)

##Create a Line Chart
chart_data = pd.DataFrame(
    np.random.rand(20, 3), columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)