from bs4 import BeautifulSoup
import requests


url = "https://quotes.toscrape.com/page/"

initial_page = 1;
end_page = 10;
author = "Albert Einstein"
quotes = []

for page in range(initial_page, end_page):
    response = requests.get(url + str(page))
    soup = BeautifulSoup(response.text, "html.parser")
    page_quotes = soup.find_all("div", class_="quote")


for quote in page_quotes:
        if (quote.find("small", class_="author").text == author):
            quote_text = quote.find("span", class_="text").text
            quotes.append(quote_text)
            print("Quote found: " + quote_text)

print("Number of quotes: " + str(len(quotes)))

