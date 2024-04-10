import plotly.express as px
import pandas as pd
import streamlit as st

st.title("Best Games on BGG")

url ='https://github.com/cchristensn/datacuration/blob/main/GameRanks.csv/?raw=True'
df = pd.read_csv(url, index_col=0)

tab1, tab2 = st.tabs(['temp', 'temp'])

with tab1:
    compRate = px.scatter(data_frame=df, x='Rating', y="Complexity")

with tab2:
    #plotM_df = name_df[name_df['sex']=='M']
    #figM = px.line(data_frame=plotM_df, x = 'year', y='n')
    #st.header(f'{name} over time')
    #st.plotly_chart(figM)
    st.text("Hello!")