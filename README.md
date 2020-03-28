# Coronavirus Recovery Probability Calculator

*[COVID-19 Global Hackathon](https://covid-global-hackathon.devpost.com/)*

### This calculator is a web application that allows users who have coronavirus (COVID-19) to calculate the probability of their recovery. We devised a machine learning algorithm that can accurately predict this value, taking into account a wide variety of factors, including information such as pre-existing medical conditions and local population statistics.

---

## Technologies used in this project

<img src="assets/img/reactjs.png" alt="ReactJS" title="ReactJS" width="150px" height="150px"><img src="assets/img/django.png" alt="Django" title="Django" width="150px" height="150px"><img src="assets/img/postgresql.png" alt="PostgreSQL" title="PostgreSQL" width="150px" height="150px"><img src="assets/img/pandas.png" alt="Pandas" title="Pandas" width="150px" height="150px"><img src="assets/img/nokogiri.png" alt="Nokogiri" title="Nokogiri" width="150px" height="150px">

* **ReactJS**
  * Used ReactJS to develop the front-end website for user interaction
* **Django**
  * Created a custom REST API for the front-end to call for making predictions and storing user data
* **PostgreSQL**
  * Maintained a database to efficiently access and update the aggregated datasets with new user data and live COVID-19 updates
* **Pandas**
  * Ran data analysis on many online datasets to accumulate appropriate training data for our machine learning model
* **Nokogiri**
  * Web scraped COVID-19 status pages to download and form datasets

## Programming languages

<img src="assets/img/python.png" alt="Python" title="Python" width="150px" height="150px"><img src="assets/img/javascript.png" alt="JavaScript" title="JavaScript" width="150px" height="150px"><img src="assets/img/ruby.png" alt="Ruby" title="Ruby" width="150px" height="150px">

* **Python** (3.7.7)
  * Project's main programming language
  * Created the machine learning algorithm and back-end API
* **JavaScript**
  * Used for developing the front-end website
* **Ruby**
  * Required for web scraping COVID-19 status pages for live data

## Online datasets

* [DataHub.io Worldwide Time Series](https://datahub.io/core/covid-19)
* [Worldometers.info US States Cases/Deaths](https://www.worldometers.info/coronavirus/country/us/)
* [Worldbank.org Worldwide Population Density](https://data.worldbank.org/indicator/en.pop.dnst)

## Team
* **Ashish D'Souza** - [computer-geek64](https://github.com/computer-geek64)
* **Varun Lakshmanan** - [varunlakshmanan](https://github.com/varunlakshmanan)
* **Pranav Pusarla** - [PranavPusarla](https://github.com/PranavPusarla)
* **Sharath Palathingal** - [therealsharath](https://github.com/therealsharath)
