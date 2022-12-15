# Stock-News-Sentiment-Analysis
Analyse October Stock News Sentiment and scrapping the news from FinViz
</p>
<p align = 'center'><img src = 'https://github.com/Samuel-the-crack/Stock-News-Sentiment-Analysis/blob/main/Picture/0_9naXQNQ5vDyJEybl.jfif', width = 450>


## A. Overview 
In this project I'm doing a Sentiment Anlysis to 7 big tech companies' news (Apple, Microsoft, Nvidia, Cisco, Google, Amazon, and Tesla). For the data itself I'm doing a web scrapping  from [Finviz](https://finviz.com/) using [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest), columns that I scrapped were Ticker, Date, Time, and Title, for further information you can read from my code [here](https://github.com/Samuel-the-crack/Stock-News-Sentiment-Analysis/blob/main/WebScrapping.py). After scrapped the data I'M doing the analysis on Jupyter Notebook.

***Requirements : Pandas, Numpy, Matplotlib, Seaborn, Beautifulsoup, Vader, and Word Cloud***

## B. Result
My analysis have two result, first I analyse words that appear most in every companies' news and the news sentiment of every companies. I use mean compound as a comparing value for sentiment. I'm using WordCloud to show words that appear the most, the picture below is a result of WordCloud.
<p align = 'center'><img src = 'https://github.com/Samuel-the-crack/Stock-News-Sentiment-Analysis/blob/main/Picture/wordcloud.JPG', width = 800>

For sentiment analysis itself I'm using vader for each title and averaging it so I can compare every company easily, The table below is the result of Vader sentiment analysis.
<p align = 'center'><img src = 'https://github.com/Samuel-the-crack/Stock-News-Sentiment-Analysis/blob/main/Picture/table.JPG', width = 500>

The average sentiment of each company is positive, there are only three company that have sentiment above the average (Cisco, Nvidia, and Amazon). Cisco have the best sentiment among the other 6 company meanwhile Google the worst (negative) sentiment among all company. For complete webscrapping code, analysis code and dataset, you can see it [here](https://github.com/Samuel-the-crack/Stock-News-Sentiment-Analysis).
