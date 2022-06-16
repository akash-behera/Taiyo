import pandas as pd
import requests
from bs4 import BeautifulSoup

IDs = []
names = []
dates = []
url = 'https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid'

try:
    page = requests.get(url)
    page.raise_for_status()

    soup = BeautifulSoup(page.text, 'html.parser')
    events = soup.find('tbody').find_all('tr')
    for i in events:
        ID = i.find('td').a.text
        name = i.find('td').find_next_siblings()[0].text
        date = i.find('td').find_next_siblings()[1].text
        IDs.append(ID)
        names.append(name)
        dates.append(date)

    #print(IDs)
    #print(names)
    #print(dates)
        #id = i.get_text(strip=True)
    df = pd.DataFrame({'event ID': IDs, 'event name': names, 'end date': dates})
    df.to_csv('C:\\Users\\ASUS\\Desktop\\Taiyo\\events.csv', index=False)


except Exception as e:
    print(e)

