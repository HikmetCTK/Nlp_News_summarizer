import requests
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
nltk.download('punkt')

NEWS_API_KEY = 'Your Api key'
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'

def fetch_news():
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'tr',  # You can set your country
    }
    response = requests.get(NEWS_API_ENDPOINT, params=params)
    news_data = response.json()
    articles = news_data['articles']
    return articles

def summarize_article(url):
    article = Article(url)
    article.download()
    article.parse()
    parser = PlaintextParser.from_string(article.text, Tokenizer("turkish"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 2)  # summary into two sentences
    return ' '.join([str(sentence) for sentence in summary])

def main():
    articles = fetch_news()
    number_of_new=5     # Set how many new you want to read.
    for article in articles[:number_of_new]:
        title = article['title']
        url = article['url']
        summary = summarize_article(url)
        print("Başlık:", title)
        print()
        print("Özet:", summary)
        print()
        print('Link:',url)
        print("\n")

if __name__ == "__main__":
    main()
