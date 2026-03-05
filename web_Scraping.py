from urllib.request import urlopen

url = "https://realpython.github.io/fake-jobs/"
page = urlopen(url)
raw_html = page.read()
html = raw_html.decode("utf-8")

import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup(html, "html.parser")
result = soup.find(id="ResultsContainer")

# print(result.prettify())

job_cards = result.find_all("div", class_="card-content")

for card in job_cards:
    # print(card.prettify(),end="\n\n")
    title = card.find("h2", class_="title is-5").text.strip()
    company = card.find("h3", class_="subtitle is-6 company").text.strip()
    location = card.find("p", class_="location").text.strip()
    page_url = card.find_all("a")[1].get("href").strip()

    print(f"Job Title : {title}")
    print(f"Company   : {company}")
    print(f"Location  : {location}")
    print(f"Page URL  : {page_url}")
    print("-" * 40)
