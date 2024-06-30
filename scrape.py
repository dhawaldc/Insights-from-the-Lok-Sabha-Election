import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://results.eci.gov.in'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')



table = soup.find('table', {'id': 'some_id'})
rows = table.find_all('tr')

data = []
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3'])
df.dropna(inplace=True)
df['Column1'] = df['Column1'].astype(int)
df.to_csv('election_results.csv', index=False)
