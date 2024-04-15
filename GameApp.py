import plotly.express as px
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Best Games on BGG")
st.image('PoweredByBGG.png')

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

st.header('Rating by Complexity Plots')
st.markdown('Use arrow keys to navigate tabs')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(['Overall', 'Abstract Games',
                                                                'Customizable Games', 'Thematic Games',
                                                                'Family Games', 'Children Games',
                                                                'Party Games', "Strategy Games", 'War Games'])

with st.sidebar:
    st.header('Game Lookup')
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
    st.subheader('Overall')
    st.markdown('Hover data avalalible on other tabs')
    st.pyplot(fig)
    
    

with tab2:
    absPlot = px.scatter(data_frame=absDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Abstract Rank'])
    absPlot.update_xaxes(range=[5.2, 8.7])
    absPlot.update_yaxes(range=[.8, 5])
    st.subheader('Abstract')
    st.plotly_chart(absPlot)

with tab3:
    custPlot = px.scatter(data_frame=custDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Customizable Rank'])
    custPlot.update_xaxes(range=[5.2, 8.7])
    custPlot.update_yaxes(range=[.8, 5])
    st.subheader('Customizable')
    st.plotly_chart(custPlot)


with tab4:
    themePlot = px.scatter(data_frame=themeDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Thematic Rank'])
    themePlot.update_xaxes(range=[5.2, 8.7])
    themePlot.update_yaxes(range=[.8, 5])
    st.subheader('Thematic')
    st.plotly_chart(themePlot)

with tab5:
    famPlot = px.scatter(data_frame=famDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Family Rank'])
    famPlot.update_xaxes(range=[5.2, 8.7])
    famPlot.update_yaxes(range=[.8, 5])
    st.subheader('Family')
    st.plotly_chart(famPlot)

with tab6:
    childPlot = px.scatter(data_frame=childDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Children Rank'])
    childPlot.update_xaxes(range=[5.2, 8.7])
    childPlot.update_yaxes(range=[.8, 5])
    st.subheader('Children')
    st.plotly_chart(childPlot)

with tab7:
    partyPlot = px.scatter(data_frame=partyDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Party Rank'])
    partyPlot.update_xaxes(range=[5.2, 8.7])
    partyPlot.update_yaxes(range=[.8, 5])
    st.subheader('Party')
    st.plotly_chart(partyPlot)

with tab8:
    stratPlot = px.scatter(data_frame=stratDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'Strategy Rank'])
    stratPlot.update_xaxes(range=[5.2, 8.7])
    stratPlot.update_yaxes(range=[.8, 5])
    st.subheader('Strategy')
    st.plotly_chart(stratPlot)

with tab9:
    warPlot = px.scatter(data_frame=warDf, x='Rating', y="Complexity", hover_data=['Name', 'Year', 
                                                                                     'Overall Rank', 'War Rank'])
    warPlot.update_xaxes(range=[5.2, 8.7])
    warPlot.update_yaxes(range=[.8, 5])
    st.subheader('War')
    st.plotly_chart(warPlot)



st.header('Stats by Year')
year = st.slider("Choose a year:", 1980, 2024)
st.markdown("'1980' means 1980 and earlier")
if year == 1980:
    yearDf=gameDf[gameDf['Year']<1981]
else:
    yearDf = gameDf[gameDf['Year']==year]

st.subheader('Complexity Distribution')
complexityPlot = px.box(data_frame=yearDf, x = 'Complexity')
complexityPlot.update_xaxes(range=[1, 5])
st.plotly_chart(complexityPlot)


st.subheader('Rating Distribution')
ratingPlot = px.box(data_frame=yearDf, x = 'Rating')
ratingPlot.update_xaxes(range=[5.5, 9])
st.plotly_chart(ratingPlot)


st.header('"Best of" search')
topic = st.selectbox("Choose a metric:", ('Rating','Ranking', 'Complexity', 'Plays Last Month',
                                          'Wants', 'Wishlists'))
genre = st.selectbox("Choose a category:", ('Overall', 'Abstract', 'Customizable', 'Thematic',
                                            'Family', 'Children', 'Party', 'Strategy', 'War'))

if genre=='Overall':
    if topic=='Ranking':
        topDf=gameDf.sort_values('Overall Rank', ascending=True).head(5).dropna(axis=1, how='all')
    else:
        topDf=gameDf.sort_values(topic, ascending=False).head(5).dropna(axis=1, how='all')
    st.dataframe(topDf)

elif genre=='Abstract':
    if topic=='Ranking':
        topDf=absDf.sort_values('Abstract Rank', ascending=True).head(5).dropna(axis=1, how='all')
    else:
        topDf=absDf.sort_values(topic, ascending=False).head(5).dropna(axis=1, how='all')
    st.dataframe(topDf)

elif genre=='Customizable':
    if topic=='Ranking':
        topDf=custDf.sort_values('Customizable Rank', ascending=True).head(5).dropna(axis=1, how='all')
    else:
        topDf=custDf.sort_values(topic, ascending=False).head(5).dropna(axis=1, how='all')
    st.dataframe(topDf)

elif genre=='Thematic':
    if topic=='Ranking':
        topDf=themeDf.sort_values('Thematic Rank', ascending=True).head(5).dropna(axis=1, how='all')
    else:
        topDf=themeDf.sort_values(topic, ascending=False).head(5).dropna(axis=1, how='all')
    st.dataframe(topDf)
    
elif genre=='Family':
    if topic=='Ranking':
        topDf=famDf.sort_values('Family Rank', ascending=True).head(5).dropna(axis=1, how='all')
    else:
        topDf=famDf.sort_values(topic, ascending=False).head(5).dropna(axis=1, how='all')
    st.dataframe(topDf)
    
elif genre=='Children':
    if topic=='Ranking':
        topDf=childDf.sort_values('Children Rank', ascending=True).head(5).dropna(axis=1, how='all')
    else:
        topDf=childDf.sort_values(topic, ascending=False).head(5).dropna(axis=1, how='all')
    st.dataframe(topDf)
    
elif genre=='Party':
    if topic=='Ranking':
        topDf=partyDf.sort_values('Party Rank', ascending=True).head(5).dropna(axis=1, how='all')
    else:
        topDf=partyDf.sort_values(topic, ascending=False).head(5).dropna(axis=1, how='all')
    st.dataframe(topDf)
    
elif genre=='Strategy':
    if topic=='Ranking':
        topDf=stratDf.sort_values('Strategy Rank', ascending=True).head(5).dropna(axis=1, how='all')
    else:
        topDf=stratDf.sort_values(topic, ascending=False).head(5).dropna(axis=1, how='all')
    st.dataframe(topDf)
    
elif genre=='War':
    if topic=='Ranking':
        topDf=warDf.sort_values('War Rank', ascending=True).head(5).dropna(axis=1, how='all')
    else:
        topDf=warDf.sort_values(topic, ascending=False).head(5).dropna(axis=1, how='all')
    st.dataframe(topDf)
    
else:
    st.markdown('Select a metric and a category')