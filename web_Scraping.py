from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup


url = "https://realpython.github.io/fake-jobs/"
page = urlopen(url)
raw_html = page.read()
html = raw_html.decode("utf-8")

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

# print(page)


# print(html)


title_start_index = html.find('<h2 class="title is-5">') + len(
    '<h2 class="title is-5">'
)
title_end_index = html.find("</h2>", title_start_index)
title = html[title_start_index:title_end_index]
# print(f"Job Title : {title.strip()}")


company_start_index = html.find('<h3 class="subtitle is-6 company">') + len(
    '<h3 class="subtitle is-6 company">'
)
company_end_index = html.find("</h3>", company_start_index)
company = html[company_start_index:company_end_index]
# print(f"Company Name : {company.strip()}")


location_start_index = html.find('<p class="location">') + len('<p class="location">')
location_end_index = html.find("</p>", location_start_index)
loc = html[location_start_index:location_end_index]
# print(f"Location : {loc.strip()}")


url_start_index = html.find('<footer class="card-footer">') + len(
    '<footer class="card-footer">'
)
url_end_index = html.find("</footer>", url_start_index)
page_url = html[url_start_index:url_end_index]
url_list = page_url.split('"')
# print(f"Page URL : {url_list[7].strip()}")
