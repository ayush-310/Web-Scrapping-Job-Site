from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"

page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
result = soup.find(id="ResultsContainer")

print("Job Title , Company , Location , Page URL")

with open('job_details.csv', 'w', newline='', encoding='utf-8') as csv_file:

    # `writer = csv.writer(csv_file)` is creating a CSV writer object that will write rows to the
    # specified CSV file (`job_details.csv`). This object provides methods to write rows of data to
    # the CSV file in a structured format. By using this writer object, you can easily write data to
    # the CSV file row by row.
    writer = csv.writer(csv_file)

    # Header
    writer.writerow(["Job Title", "Company", "Location", "Page URL"])

    job_cards = result.find_all("div", class_="card-content")

    for card in job_cards:
        title = card.find("h2", class_="title is-5").text.strip()
        company = card.find("h3", class_="subtitle is-6 company").text.strip()
        location = card.find("p", class_="location").text.strip()
        page_url = card.find_all("a")[1].get("href").strip()

        print(f"{title} | {company} | {location} | {page_url}")

        # `writer.writerow([title, company, location, page_url])` is a method call that writes a
        # single row of data to the CSV file specified by the `csv_file` object. The data for this row
        # is provided as a list `[title, company, location, page_url]`. Each element in the list
        # corresponds to a column in the CSV file, and the `writer.writerow()` method writes these
        # elements as a single row in the CSV file. This allows you to write the job title, company,
        # location, and page URL for each job card as a separate row in the CSV file.
        writer.writerow([title, company, location, page_url])

print("Job details saved to job_details.csv")