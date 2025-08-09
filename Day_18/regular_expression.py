# Exercises level 2
import re

def is_valid_variable(var):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    return bool(re.match(pattern, var))

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))    

# Exercises level 3
import re
from collections import Counter

def clean_text(text):
    cleaned = re.sub(r'[^A-Za-z\s]', '', text)
    return cleaned.strip()

def most_frequent_words(text):
    words = text.split()
    counter = Counter(words)
    return counter.most_common(3)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))
