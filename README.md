# Crypto Caroussel
---
![Carousel](./images/Carousel.JPG)


<!-- CONTENTS -->
## Contents

* [Team](#team)
* [Proposal](#proposal)
* [File Explanation](#file-explanation)
* [Project Flow](#project-flow)
* [Tools Used](#tools-used)
* [Contact](#contact)
  
Presentation Link - [https://docs.google.com/presentation/d/1p8Kv0wzOZSW4kmNYT3HJaxAGV2-7wxH0hyfHsmVSAX0/edit#slide=id.p](https://docs.google.com/presentation/d/1p8Kv0wzOZSW4kmNYT3HJaxAGV2-7wxH0hyfHsmVSAX0/edit#slide=id.p)

<!-- TEAM -->
## Team
Evan Paliotta, Francisco Lopez, Daniel Klein Velderman

<!-- PROPOSAL -->
## Proposal
Our project is to create and compare a short-term algorithmic trading strategy with a medium-term buy and hold strategy. In reference to our short term strategy, we utilize the RSI and MACD while implementing regression and natural language processing in our buy and hold strategy. The latter strategy uses daily BTC exchange rate data and focuses on nine currencies with three distinct use cases.  We gathered data from the Binance API for both strategies and the Reddit API for NLP. Finally we compared the returns of the models and ultimately determined which strategy is more profitable to implement.

<!-- FILE EXPLANATION -->
## File Explanation
1. For the short-term strategy, look at the Algo folder.  Here you'll find all the code for the algorithmic trading strategies.
2. The Crypto Corousel file displays the running code from a combination of all the notebooks in the repository.
3. The NLP file has natural language processing code for three cryptocurrencies that were outputted from the regression model in the ml_models file. 
4. ml_models has the regression analysis and LSTM neural network price prediction model.

<!-- PROJECT FLOW -->
## Project Flow
Think of this project like a filtering process for determining which cryptocurrencies are worth paying attention to.  Start with the regression model from ml_models.  The cryptocurrencies with the lowest mean squared error and max error were used to determine which coins should be further examined. Next open the NLP file to see which coins had the best sentiment.  Finally go back to the ml_models file to see the neural network price prediction model. The outputs from these two files were then compared with those of the Algo files to determine which strategy would be more lucrative to implement.

<!-- TOOLS USED -->
## Tools Used
- Pandas
- Google Colab
- Binance API
- SciKit Learn 
  - Linear Regression
  - LSTM Neural Network
  - Random FOrest
- Natural Language Toolkit
  - Vader Sentiment Analyzer
- Push Shift API
- News API
- Algorithmic Trading Indicators
  - Moving Average Convergence Divergence (MACD)
  - Relative Strength Index (RSI)

<!-- CONTACT -->
## Contact

Evan Paliotta - paliotta.evan@gmail.com

Project Link: [https://github.com/evanpaliotta/Recession_Analysis](https://github.com/evanpaliotta/Recession_Analysis)

LinkedIn - [https://www.linkedin.com/in/evanpaliotta/](https://www.linkedin.com/in/evanpaliotta/)
