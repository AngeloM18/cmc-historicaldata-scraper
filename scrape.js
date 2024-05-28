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