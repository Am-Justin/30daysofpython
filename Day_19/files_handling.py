import os
import json
import sys

def count_lines_words(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        z = f.read()
    
    num_lines = len(lines)

    num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words


data_folder = "data"

files = [
    "obama_speech.txt",
    "michelle_obama_speech.txt",
    "donald_speech.txt",
    "melina_trump_speech.txt"
]

for file_name in files:
    file_path = os.path.join(data_folder, file_name)
    lines, words = count_lines_words(file_path)
    print(f"{file_name}: {lines} lines, {words} words")


# 2
from data.countries_data import countries_data

def dict_to_json(_dict):
    with open("data/countries_data.json", "w", encoding='utf-8') as f:
            json.dump(_dict, f, ensure_ascii=False, indent=4)
    

import json

def most_spoken_languages(filename, nbre):
    with open(filename, 'r', encoding='utf-8') as f:
        countries_data = json.load(f)
    
    freq_lang = {}
    for country in countries_data:
        for lang in country["languages"]:
            if lang in freq_lang:
                freq_lang[lang] += 1
            else:
                freq_lang[lang] = 1
    
    sorted_langs = sorted(freq_lang.items(), key=lambda x: x[1], reverse=True)
    
    return [(count, lang) for lang, count in sorted_langs[:nbre]]

print(most_spoken_languages('./data/countries_data.json', 10))


# 3
def most_populated_countries(filename, nbre):
    with open(filename, "r", encoding="utf-8") as f:
        countries_data = json.load(f)
    most_population = sorted(countries_data, key=lambda x:x["population"], reverse=True)[:nbre]
    return [(country["name"], country["population"]) for country in most_population]

print(most_populated_countries('./data/countries_data.json', 10))