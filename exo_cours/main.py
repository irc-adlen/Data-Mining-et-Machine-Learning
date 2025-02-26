import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import spacy

# url = "https://www.lemonde.fr/"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     for p in soup.find_all('p'):
#         print(p.text)
# else:
#     print("Error", response.status_code)

# words = ["running", "runner", "ran", "runs"]
# stemmer = PorterStemmer()

# for word in words:
#     print(word, "=>", stemmer.stem(word), end="\n")

# nlp = spacy.load("en_core_web_sm")

# text_to_analyze = "Paris is the capital of France." + "In 2015, its population was recorded as 2,206,488"

# doc = nlp(text_to_analyze)

# vector_list = [token.vector for token in doc]
# print("Vecteurs de '{}' : {}".format(text_to_analyze, vector_list))

sia = SentimentIntensityAnalyzer()

sentiment = sia.polarity_scores("This is a great movie")
print(sentiment)

sentiment = sia.polarity_scores("This is a good movie")
print(sentiment)

sentiment = sia.polarity_scores("This movie is not very good")
print(sentiment)

sentiment = sia.polarity_scores("This movie is not very terrible")
print(sentiment)

sentiment = sia.polarity_scores("This is a terrible movie")
print(sentiment)