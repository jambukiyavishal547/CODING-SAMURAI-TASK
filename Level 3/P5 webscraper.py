import requests
from bs4 import BeautifulSoup
import csv

URL = "https://news.ycombinator.com"

# Send request
response = requests.get(URL)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all news titles
titles = soup.find_all("span", class_="titleline")

# Open CSV file
with open("news_headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No", "Headline", "Link"])

    for index, title in enumerate(titles, start=1):
        headline = title.a.text
        link = title.a["href"]
        writer.writerow([index, headline, link])

print("✅ News headlines saved to news_headlines.csv")
