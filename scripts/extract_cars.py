import requests
from bs4 import BeautifulSoup
import json
import re

def fetch_cars(url='https://forza.fandom.com/wiki/Forza_Horizon_5/Cars'):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find_all('table')[1]
    cars = []
    for row in table.find_all('tr')[1:]:
        link = row.find('a')
        if not link:
            continue
        model = link.text.strip()
        year_match = re.search(r'(19|20)\d{2}', row.text)
        year = year_match.group(0) if year_match else ''
        brand = model.split()[0]
        cars.append({'brand': brand, 'model': model, 'year': year})
    return cars

if __name__ == '__main__':
    cars = fetch_cars()
    with open('data/fh5_cars.json', 'w', encoding='utf-8') as f:
        json.dump(cars, f, ensure_ascii=False, indent=2)
    print(f'Saved {len(cars)} cars to data/fh5_cars.json')
