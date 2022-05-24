import requests
import json

from bs4 import BeautifulSoup

base_url = 'https://www.eortologio.xyz/'
urls = {
    '01': base_url + 'giortes-ton-ianouario/',
    '02': base_url + 'giortes-ton-fevrouario/',
    '03': base_url + 'giortes-ton-martio/',
    '04': base_url + 'giortes-ton-aprilio/',
    '05': base_url + 'giortes-ton-maio/',
    '06': base_url + 'giortes-ton-iounio/',
    '07': base_url + 'giortes-ton-ioulio/',
    '08': base_url + 'giortes-ton-augousto/',
    '09': base_url + 'giortes-ton-septemvrio/',
    '10': base_url + 'giortes-ton-oktovrio/',
    '11': base_url + 'giortes-ton-noemvrio/',
    '12': base_url + 'giortes-ton-dekemvrio/'
}

out = {
    "namedays": []
}

for key in urls:
    page_content = requests.get(urls[key]).content
    soup = BeautifulSoup(page_content, "html.parser")
    
    name_day_rows = soup.find_all('div', class_='go')

    for name_day_row in name_day_rows:
        data = {
            "date": '',
            "names": []
        }
        date = name_day_row.find("a", class_="htdu").text
        names = name_day_row.find_all("span", itemprop="name")

        data["date"] = date

        for name in names:
            data["names"].append(name.text)

        out["namedays"].append(data)

        filename = key + '.json'

        with open(filename, 'w') as outfile:
            outfile.write(json.dumps(out, indent=2, ensure_ascii=False))
        
    out["namedays"] = []