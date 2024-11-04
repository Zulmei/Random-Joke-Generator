import requests
import string
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud

API_KEY = "40567d87c6ac44c18a066bdddaad5b28"
category = input("Enter a news category (e.g., sports, technology, health): ")

url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}"
response = requests.get(url)
data = response.json()

titles = [article['title'] for article in data['articles'] if 'title' in article]

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)

all_titles = ' '.join(titles).lower()

words = [word for word in all_titles.split() if word not in stop_words and word not in punctuation]

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
