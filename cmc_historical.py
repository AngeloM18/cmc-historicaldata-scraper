import argparse
from datetime import datetime as dt
from datetime import timedelta as td
from selenium import webdriver
import pandas as pd
import time

URL = "https://coinmarketcap.com/historical/"
DRIVER_OPTIONS = webdriver.ChromeOptions()
DRIVER_OPTIONS.add_argument('--blink-settings=imagesEnabled=false')
DRIVER = webdriver.Chrome(options=DRIVER_OPTIONS)
DATE_FORMAT = "%Y%m%d"

def scrape(date): 
    DRIVER.get(URL + dt.strftime(date, DATE_FORMAT))
    results = DRIVER.execute_script(
    '''
        document.body.style.zoom='5%'             
        await new Promise(r => setTimeout(r, 4000));

        function top200() {
            const tableHeaders = ['Market Cap', 'Price', '% 7d'];
            const data = {};

            const trElements = document.querySelectorAll('div table tbody tr');
						
            for (let index of trElements.keys()) {
              	const tdElements = Array.from(trElements[index].querySelectorAll('td'));
                // coin name (ticker)
				const coinName = `${tdElements[1].querySelector('div > a:nth-of-type(2)').textContent} (${tdElements[2].textContent})`;
                const headers = [...tableHeaders];
                // mcap up to price
                const sliced = tdElements.slice(3, 5);
                // 7-day percentage
                sliced.push(tdElements[9]);
                
                const coinData = Object.fromEntries(sliced.map( (x) => [headers.shift(), x.textContent]) );
                data[coinName] = coinData;
            }
            return data
        }
        return top200()
    ''')

    transposed = {}
    for outerKey, innerDict in results.items(): 
        for innerKey, values in innerDict.items():
            transposed[(outerKey, innerKey)] = values

    return {date: transposed}
    
def parse_date(date):
    return dt.strptime(date, DATE_FORMAT)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=parse_date, default=dt(2016, 1, 1))
    parser.add_argument('--end', type=parse_date, default=dt.today())
    parser.add_argument('--freq', type=int, default=7)
    parser.add_argument('--out', default='scraped_data.xlsx')
    arg = parser.parse_args()

    data = {}
    date = arg.start
    
    while date <= arg.end:
        data.update(scrape(date))
        date += td(arg.freq)
        time.sleep(1)

    df = pd.DataFrame(data).T
    df.columns.set_names("Date", level=0, inplace=True)
    print(df)
    df.to_excel(arg.out, freeze_panes=(1, 1))

if __name__ == '__main__':
    main()
