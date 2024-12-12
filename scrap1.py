import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the website
url = "https://quotes.toscrape.com/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())
# Find all quote elements on the page
quotes = soup.find_all('span', class_='text')
authors=soup.find_all('small', class_="author")
for author in authors:
    print(author.get_text())

# Loop through and print each quote
for quote in quotes:
    print(quote.get_text())
