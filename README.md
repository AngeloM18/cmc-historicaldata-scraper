# CMC HISTORICAL DATA SCRAPER
Very simple Selenium-based script to scrape data from the top 200 coins table at https://coinmarketcap.com/historical/ from and up to the dates specified. The data from all tables is then aggregated and saved to an Excel spreadsheet.

 ## USAGE
```
cmc_historical.py [--start] [--end] [--freq] [--out]
```
### OPTIONS
The dates follow the format %Y%m%d — for instance: 20240202.
```
--start — Enter the start date to start scraping from (20160101, by default).
--end — Enter the end date to scrape up to (today's date, by default).
--out — Enter the name of the output .xlsx file (scraped_data.xlsx, by default).
--freq — Enter the frequency of the data (7 [weekly], by default).
```
### EXAMPLE
```
python3 cmc_historical.py 20170101 20180101 7
```

## DEPENDENCIES
```
virtualenv (if you want to install the below dependencies on their own Python environment).
argparse
selenium
pandas
xlrd
openpyxl
```

## HOW TO
Manually download the package as a zip file or clone the repository using git. 
After that, place the package in a directory of your choosing, open the terminal (Unix) or CMD (Windows) and move to that directory. If you set up a virtual environment, activate it, install all dependencies and then run the script.

### ... INSTALL DEPENDENCIES
(Optional) Set up a virtual environment to install the dependencies in:
```
pip install virtualenv

mkdir cmc_scraper
cd ./cmc_scraper
python3 -m venv cmc

source (linux/macos) ./cmc/bin/activate
```
Install dependencies.
```
pip install pandas argparse selenium xlrd openpyxl
```

## DATA EXAMPLE
![marketdata](https://github.com/AngeloM18/cmc-historicaldata-scraper/assets/123282394/547910cc-6e2b-4f22-8211-26b76313e376)

Since this script only scrapes the data from the top 200 table, those that have empty cells mean they fell from that rank.
