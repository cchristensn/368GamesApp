import plotly.express as px
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

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
st.markdown('Use arrow keys to navigate tabs')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(['Overall', 'Abstract Games',
                                                                'Customizable Games', 'Thematic Games',
                                                                'Family Games', 'Children Games',
                                                                'Party Games', "Strategy Games", 'War Games'])

with st.sidebar:
    game = st.text_input('Enter a game name', value='Pandemic')
    if st.button('Random'):
        game = gameDf.sample().iloc[0,0]
        

    subGameDf = gameDf[gameDf['Name'].str.contains(game)].dropna(axis=1, how='all')
    if subGameDf.empty:
        st.markdown('Game not found')
    else:
        st.dataframe(subGameDf)



with tab1:
    
    fig, ax = plt.subplots(figsize=(8, 8))

    sns.scatterplot(data=absDf, x='Rating', y='Complexity', label='Abstract')
    sns.scatterplot(data=custDf, x='Rating', y='Complexity', label='Customizable')
    sns.scatterplot(data=themeDf, x='Rating', y='Complexity', label='Thematic')
    sns.scatterplot(data=famDf, x='Rating', y='Complexity', label='Family')
    sns.scatterplot(data=childDf, x='Rating', y='Complexity', label='Children')
    sns.scatterplot(data=partyDf, x='Rating', y='Complexity', label='Party')
    sns.scatterplot(data=stratDf, x='Rating', y='Complexity', label='Strategy')
    sns.scatterplot(data=warDf, x='Rating', y='Complexity', label='War')

    ax.legend()
    st.header('Overall')
    st.markdown('Hover data avalalible on other tabs')
    st.pyplot(fig)
    
    

with tab2:
    absPlot = px.scatter(data_frame=absDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Abstract Rank'])
    absPlot.update_xaxes(range=[5.2, 8.7])
    absPlot.update_yaxes(range=[.8, 5])
    st.header('Abstract')
    st.plotly_chart(absPlot)

with tab3:
    custPlot = px.scatter(data_frame=custDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Customizable Rank'])
    custPlot.update_xaxes(range=[5.2, 8.7])
    custPlot.update_yaxes(range=[.8, 5])
    st.header('Customizable')
    st.plotly_chart(custPlot)


with tab4:
    themePlot = px.scatter(data_frame=themeDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Thematic Rank'])
    themePlot.update_xaxes(range=[5.2, 8.7])
    themePlot.update_yaxes(range=[.8, 5])
    st.header('Thematic')
    st.plotly_chart(themePlot)

with tab5:
    famPlot = px.scatter(data_frame=famDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Family Rank'])
    famPlot.update_xaxes(range=[5.2, 8.7])
    famPlot.update_yaxes(range=[.8, 5])
    st.header('Family')
    st.plotly_chart(famPlot)

with tab6:
    childPlot = px.scatter(data_frame=childDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Children Rank'])
    childPlot.update_xaxes(range=[5.2, 8.7])
    childPlot.update_yaxes(range=[.8, 5])
    st.header('Children')
    st.plotly_chart(childPlot)

with tab7:
    partyPlot = px.scatter(data_frame=partyDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Party Rank'])
    partyPlot.update_xaxes(range=[5.2, 8.7])
    partyPlot.update_yaxes(range=[.8, 5])
    st.header('Party')
    st.plotly_chart(partyPlot)

with tab8:
    stratPlot = px.scatter(data_frame=stratDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Strategy Rank'])
    stratPlot.update_xaxes(range=[5.2, 8.7])
    stratPlot.update_yaxes(range=[.8, 5])
    st.header('Strategy')
    st.plotly_chart(stratPlot)

with tab9:
    warPlot = px.scatter(data_frame=warDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'War Rank'])
    warPlot.update_xaxes(range=[5.2, 8.7])
    warPlot.update_yaxes(range=[.8, 5])
    st.header('War')
    st.plotly_chart(warPlot)




