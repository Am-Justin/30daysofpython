import requests
from bs4 import BeautifulSoup
import json

url = "https://archive.ics.uci.edu/dataset/186/wine+quality"
url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
url = "https://archive.ics.uci.edu/dataset"

response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"border": "1"})
rows = table.find_all("tr")[1:]

data_list = []

for row in rows:
    cols = [col.get_text(strip=True) for col in row.find_all("td")]
    if cols:
        data_list.append(cols)


with open("uci_datasets.json", "w", encoding="utf-8") as f:
    json.dump(data_list, f, ensure_ascii=False, indent=2)

