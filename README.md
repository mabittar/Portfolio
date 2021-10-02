# Marcel Bittar

[![author](https://img.shields.io/badge/Author-MarcelBittar-blue)](https://www.linkedin.com/in/marcelbittar/) [![](https://img.shields.io/badge/python-3.8.6+-blue.svg)](https://www.python.org/downloads/release/python-386/)  [![](https://img.shields.io/github/languages/top/mabittar/Portfolio)](https://mabittar.github.io/)  [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/mabittar/Portfolio/issues)



Repository containing portfolio of data science projects completed by me for academic, self learning, and hobby purposes. 

*My passion in technology and programming skills drive me to start a new knowledgment area in Computer Engineering. I use this repo to track my projects.*

But I always work with large urban infrastructure and heavy civil projects like Metro Sao Paulo (Line 2 and 5), Metro Salvador, GRU Airport, LEED Platinum commercial building;





**Background in:** Python, Machine Learning, Django, AWS and infrastructure for heavy projects.

**Links:**
* [WebSite](https://mabittar.github.io/)
* [LinkedIn](https://www.linkedin.com/in/marcelbittar/?locale=en_US)
* [Medium](https://medium.com/@marcelmartinsbittar)


_Note: Data used in the projects (accessed under data directory) is for demonstration purposes only._

## Contents

- ### Framework
- * [FastAPI Starter](https://github.com/mabittar/fast): A multi purpose fastapi template already structured. Just clone and start develop. In this template you have examples of CRUD using SQLite and SQLModel to handle with datta, connectors to external API, simples cache strucute, docker yml and dockerfile and makefile to fast start a project local or in production.

- ### Model Deploy
  * [RealState in Sao Paulo](https://github.com/mabittar/imovsp): All steps to deployment of an API that´s use an Machine Learning model to predict values for Sao Paulo RealState.
  
- ### Deep Learning
   * [Traffic Sign Recognition](https://github.com/mabittar/Portfolio/blob/master/Reconhecendo_Sinais_Tr%C3%A2nsito.ipynb): Using Convolutinal Network recognize traffic signs. The model obtained 95% accuracy during training and above 80% in the test. I also used a random sign directly from the web to check if the model would correctly identify it.
   * [Fake News Classifier](https://github.com/mabittar/Portfolio/blob/master/Classificador_FakeNews.ipynb): Using keras to predict if a news is Fake or Real. The model obtained 98% of accuracy.

- ### Machine Learning
    * [Default Risk](https://github.com/mabittar/Portfolio/blob/master/Risco_Inadimpl%C3%AAncia.ipynb): A Machine Learning model using RandomForest, SVC, Decision Tree, bayes tunning to XGBoost and Keras to identify whether a customer is possibly unable to meet his obligations (default risk) and consequently affect credit risk and thus interest rates.
    * [Churn Rate](https://github.com/mabittar/Portfolio/blob/master/Churn_Predict.ipynb): Analysis of Churn Rate with differents ML models: XGboost, SVC, Decision Tree, Voting Method. Tunning hyperparameters with Grid Search (manual) and BayesSearchCV (automatic). At least I used SHAP (SHapley Additive exPlanations) to explain what's influence more the ML model.
    * [Ensemble Method](https://github.com/mabittar/Portfolio/blob/master/ML11_Ensemble.ipynb): Using ensemble method to optimize diferents ML models to classify an makrting campaing
    * [Fraud Detection on Credit Card Transactions](https://github.com/mabittar/Portfolio/blob/master/Detec%C3%A7%C3%A3o_de_Fraude_em_CC.ipynb): Comparison of metrics assessment using logistic regression and decision tree to identify fraud in credit card transactions
    * [Single / Multiple Linear Regression](https://github.com/mabittar/Portfolio/blob/master/ML2_Regressao_Linear.ipynb): Using an Kraggle dataset to analysis house price prediction. Evaluating R2 score, MSE and MAE to compare single / multiple regression

- ### Data Analysis and Visualisation
   * [Data Vis using Matplot, Seaborn and Bokeh](https://github.com/mabittar/Portfolio/blob/master/Visualiza%C3%A7%C3%B5es_de_Dados.ipynb): A guide step by step to build plots using Matplot and Seaborn from real datasets. Also made a iteractive plot using Bokeh. It is an interactive visualization library for modern web browsers.
   * [Panorama of Covid-19](https://github.com/mabittar/Portfolio/blob/master/Panorama_do_COVID_19_no_Mundo.ipynb): Using an dataset from World in Data to explore the panorama of Covid-19 in world.
   * [WordClouds from AirBnB data](https://github.com/mabittar/Portfolio/blob/master/Wordcloud.ipynb) : Another way to display data. Using wordclouds to analysis data of AirBnB sumarary.
   * [Data analysis from AirBnB in Rio de Janeiro](https://github.com/mabittar/Portfolio/blob/master/Analise_de_Dados_dispon%C3%ADvel_no_Airbnb.ipynb): Analysis of AirBnB data from Rio de Janeiro and its implications.
   * [Analyzing Violence in Rio de Janeiro](https://github.com/mabittar/Portfolio/blob/master/Analisando_a_Viol%C3%AAncia_no_Rio_de_Janeiro.ipynb) : Exploratory Analysis of the violance data in RJ.

- ### Crawlers | Scrapers
   * [YouTube Channel Metadados](https://github.com/mabittar/Portfolio/blob/master/YouTube_Scaper.ipynb): Frist tried to use BeautifulSoup to aquire metadados from an YouTube Channel, like videos titles, tags, likes, comments, but is not allowed (automatic access). Second attemp using YouTube API to get all data from the channel. Got some insights from data and add some data visualization. All steps to create an Autorized Google API, how to ingest data and parser to a dataframe. Convert correctly datetime and other usefull features for futher analysis.
   * [Metro SP Status](https://github.com/mabittar/Portfolio/blob/master/MetroSP_crawler.ipynb): Using BeautifulSoup to aquire operation info and save the data to a public google spreadsheet after authorization.
   * [DuckDuckGo - API](https://github.com/mabittar/Portfolio/blob/master/DuckDuckGoAPI.py): A script to consume API based on concepts of clean Architecture, spliting input, process and output in differents functions.
   * [PNG-Mart](https://github.com/mabittar/Portfolio/blob/master/PNGMart_Scraper.ipynb): A scraper to donwload imagens from the site. Based on concepts of clean Architecture
   
- ### Django
  * [Eventex](https://github.com/mabittar/eventex/tree/master): My first project using Django webframe. Ready is when it's online, came and check it at: [Eventex](https://eventex-mmb.herokuapp.com/)

- ### GUI
  * [Password Generator](https://github.com/mabittar/pass_gen): A password generator using tkinter and secrets python's modules. Using scaler bar to choose password length and copy button to add in the clipboard. No other dependencies is need to run this app.
   
- ### Dockers and Containers
  * [Eventex - container](https://github.com/mabittar/wttd_docker): After I started the project [Eventex](https://github.com/mabittar/eventex/tree/master) I also made a container to easily deployment.
 
 
 
- ### Financial
  * [Financial Data](https://github.com/mabittar/FinancialData)
   * [Algo Trade](https://github.com/mabittar/Portfolio/blob/master/Stock_Technical_Analysis.ipynb): Using all examples below to make an AlgoTrading with Moving Averages.
  <li>Tecnical Analysis (graphic)
       <ol>
       <li>[x] Acquiring financial data (date, open, close, max, min, volume, adjust close)
                     <ul>                    
                     <li>[x] - YFinance (yahoo finance data)</li>
                      <li>[link](https://github.com/mabittar/FinancialData/blob/master/technical_analysis/YFinance_Stock_data.ipynb)</li>
                     <li>[x] - Quandl</li>
                      <li>[link](https://github.com/mabittar/FinancialData/blob/master/technical_analysis/Quandl_Stock_data.ipynb)</li>
                     <li>[x] - Pandas DataReaders</li>
                      <li>[link](https://github.com/mabittar/FinancialData/blob/master/technical_analysis/Pandas_datareader_Get_Stock_data.ipynb)</li>
                     <li>...</li>
                     <li>[x] - export data to others steps</li>
                     </ul>
              <ol>
              <li>[x] Compare different ways of acquiring data</li> 
              </ol>
       </li>
       <li>[x]Treating data</li> 
       <li>[x]Statistical Analysis </li> 
              <ol>
              <li>Graphics and display data
                     <ul>
                     <li>[x] close price at time</li>
                            <li>[x] adjusted close price</li>
                            <li>[x] normalize and compare diferente stocks close price at same start time</li>
                            <li>[x] normalize and compare return</li>
                            <li>[x] peaks (highs) or troughs (lows)
                            <li>[x] moving avarge</li>
                            <li>[ ] Bollinger Bands</li>
                            <li>[x] exponential movving avarge </li>
                     </ul>
              </li>      
              </ol>
      </ol>
<li>Fundamentalist Analysis
       <ol>
       <li>[x] Acquiring open company data
              <ul>
                     <li>[x] Fundamentus (fundamentus.com.br)</li> 
                     <li>[link](https://github.com/mabittar/FinancialData/blob/master/fundamental_analysis/Fundamentalist.ipynb)</li>
                     <li>[ ] Other Economics indexes</li>
              </ul>
       </li>
       <li>[x] Treating data</li>
       <li>[ ] Statistical Analysis</li>
              <ul>
              <li>[ ] Correlational x Influence in stock price</li>
              </ul>
      </ol>
</li>
</ol>

---

If you liked what you saw, want to have a chat with me about the portfolio, work opportunities, or collaboration, shoot an email at [mail](ma_bittar@yahoo.com.br). 
