import plotly.express as px
import pandas as pd
import streamlit as st

st.title("Best Games on BGG")

url ='https://github.com/cchristensn/datacuration/blob/main/GameRanks.csv/?raw=True'
gameDf = pd.read_csv(url, index_col=0)
absDf = gameDf[gameDf['Abstract Rank'].notna()]
custDf = gameDf[gameDf['Customizable Rank'].notna()]
themeDf = gameDf[gameDf['Thematic Rank'].notna()]
famDf = gameDf[gameDf['Family Rank'].notna()]
childDf = gameDf[gameDf['Children Rank'].notna()]
partyDf = gameDf[gameDf['Party Rank'].notna()]
stratDf = gameDf[gameDf['Strategy Rank'].notna()]
warDf = gameDf[gameDf['War Rank'].notna()]

st.subheader('Rating by Complexity Plots')
st.text('Use arrow keys to navigate tabs')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(['Rating x Complexity', 'Abstract Games',
                                                                'Customizable Games', 'Thematic Games',
                                                                'Family Games', 'Children Games',
                                                                'Party Games', "Strategy Games", 'War Games'])

with tab1:
    compRate = px.scatter(data_frame=gameDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 'Overall Rank'])
    st.header('Overall')
    st.plotly_chart(compRate)

with tab2:
    absPlot = px.scatter(data_frame=absDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Abstract Rank'])
    st.header('Abstract')
    st.plotly_chart(absPlot)

with tab3:
    custPlot = px.scatter(data_frame=custDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Customizable Rank'])
    st.header('Customizable')
    st.plotly_chart(custPlot)


with tab4:
    themePlot = px.scatter(data_frame=themeDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Thematic Rank'])
    st.header('Thematic')
    st.plotly_chart(themePlot)

with tab5:
    famPlot = px.scatter(data_frame=famDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Family Rank'])
    st.header('Family')
    st.plotly_chart(famPlot)

with tab6:
    childPlot = px.scatter(data_frame=childDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Children Rank'])
    st.header('Children')
    st.plotly_chart(childPlot)

with tab7:
    partyPlot = px.scatter(data_frame=partyDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Party Rank'])
    st.header('Party')
    st.plotly_chart(partyPlot)

with tab8:
    stratPlot = px.scatter(data_frame=stratDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Strategy Rank'])
    st.header('Strategy')
    st.plotly_chart(stratPlot)

with tab9:
    warPlot = px.scatter(data_frame=warDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'War Rank'])
    st.header('War')
    st.plotly_chart(warPlot)
