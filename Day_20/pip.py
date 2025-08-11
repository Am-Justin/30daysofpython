# Exercises: Day 20
# 1. Read this url and find the 10 most frequent words. romeo_and_juliet
import requests
import re
from collections import Counter
import statistics

def freq_words(nbre):
    url = "http://www.gutenberg.org/files/1112/1112.txt"

    response = requests.get(url)
    text = re.sub(r'[^\w\s]', '', response.text).lower()
    words = text.split()
    
    return Counter(words).most_common(nbre)

print(freq_words(10))

# 2
# i. the min, max, mean, median, standard deviation of cats' weight in
# metric units.
# ii. the min, max, mean, median, standard deviation of cats' lifespan in
# years.
def cats(url, data):
    response = requests.get(url)
    cats_data = response.json()
    print(cats_data[:1])
    weights = []
    for cat_data in cats_data:
        if data == "life_span":
            val = cat_data["life_span"]
        elif data == "weight":
            val = cat_data["weight"]["metric"]

        try:
            high, low = val.split("-")
            moy = (float(high.strip()) + float(low.strip()))/2
            weights.append(moy)

        except ValueError:
            pass
        
        maxi = max(weights)
        mini = min(weights)
        mean = statistics.mean(weights)
        median = statistics.median(weights)

        if len(weights) > 1:
            std = statistics.stdev(weights)
        else:
            std = 0

    return data ,maxi, mini, mean, median , std

data ,maxi, mini, mean, median , std = cats("https://api.thecatapi.com/v1/breeds", "weight")
print(f"Pour les calculs concernant {data}")
print(f"Le maximum est : {maxi}")
print(f"Le minimum est : {mini}")
print(f"La moyenne est : {mean}")
print(f"Le median est : {median}")
print(f"Le std est : {std}")
# print(cats("https://api.thecatapi.com/v1/breeds", "life_span"))


# iii. Create a frequency table of country and breed of cats 
def breed_country(url):
    freq = []
    response = requests.get(url)
    cats_data = response.json()
    count_country = Counter(cat_data["origin"] for cat_data in cats_data)
    for country, count in count_country.items():
        freq.append(f"Pays : {country} pour {count} Race")
    return freq

print(breed_country("https://api.thecatapi.com/v1/breeds"))

# 3
# Read the countries API and find

def countries_manip(url):
    response = requests.get(url)
    countries_data = response.json()
    print("Status de la reponse",response.status_code)
    print("Countries_data",countries_data[:1])
    return
# countries_manip("https://restcountries.eu/rest/v2/all")
# COUNTRIES API NOT AVAILABLE