import requests

query = input("What news are you interested in today : ")
api = "7fb741c01f0b47c5b4fab3fca1456545" 

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-21&sortBy=publishedAt&apiKey={api}"

r = requests.get(url)
data  = r.json()
articles = data["articles"]

for article in articles:
    print(article["title"] ,article["url"]  )
    print("\n ******************************** \n")

