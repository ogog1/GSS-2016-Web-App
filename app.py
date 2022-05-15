import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import csv

gss_data = pd.read_csv("gss2016.csv", delimiter=",")
st.title('General Social Survey 2016')
st.header('Data Analysis w/ Visuals')

st.text('')
st.text('')

# tables
gss_data_filtered = gss_data[['sex','race','age','degree','wrkstat','income','happy']]

st.text('')
st.text('')

st.header('GSS 2016 Data Filtered')

st.text('')
st.text('')

st.dataframe(gss_data_filtered)

st.text('')
st.text('')

st.header('GSS 2016 Data Aggregated by Count')

st.text('')
st.text('')

columns = {'sex','race','age','degree','wrkstat','income','happy'}

pick_columns = st.selectbox('Count by Column: ', list(columns))
gss_data_filtered['Count'] = 0
gss_data_filtered_count = gss_data_filtered.groupby(pick_columns).count()
gss_data_filtered_count = gss_data_filtered_count[['Count']]
gss_data_filtered_count['Percentages'] = (gss_data_filtered_count.Count / gss_data_filtered_count.Count.sum()) * 100

st.dataframe(gss_data_filtered_count)

st.text('')
st.text('')

st.header('GSS 2016 Data Correlation')

st.text('')
st.text('')

multi_select_column = st.multiselect("Multi-select columns for correlation:", list(columns), default=['sex'])
multi_select_gss_data_filtered = gss_data_filtered[multi_select_column]

st.dataframe(multi_select_gss_data_filtered)

multi_select_column2 = st.multiselect('Multi-select columns grouped by:', list(columns), default=['sex'])
multi_select_groupby = gss_data_filtered[multi_select_column2].groupby(multi_select_column2).size().reset_index(name='Count')
multi_select_groupby['Percentages'] = (multi_select_groupby.Count / multi_select_groupby.Count.sum()) * 100

st.dataframe(multi_select_groupby)
# tables

# visualization
st.text('')
st.text('')

st.header('GSS 2016 Data Aggregated by Count Pie Chart')

st.text('')
st.text('')

columns_pie = {'sex','race','degree','wrkstat','income','happy'}
pick_columns_visualized = st.selectbox('Visualize by Column: ', list(columns_pie))
gss_data_filtered_count_visual = gss_data_filtered.groupby(pick_columns_visualized).count()
gss_data_filtered_count_visual['x-axis'] = gss_data_filtered_count_visual.index
fig = go.Figure(data=[go.Pie(labels=gss_data_filtered_count_visual['x-axis'], values=gss_data_filtered_count_visual['Count'])])

st.plotly_chart(fig)


