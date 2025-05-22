import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.olx.in/items/q-car-cover"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

filename = "olx_car_covers.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Location", "Link"])

    for item in soup.find_all("li", {"data-aut-id": "itemBox"}):
        title = item.find("span", {"data-aut-id": "itemTitle"})
        price = item.find("span", {"data-aut-id": "itemPrice"})
        location = item.find("span", {"data-aut-id": "itemLocation"})
        link = item.find("a", href=True)

        if title and price and location and link:
            writer.writerow([
                title.text.strip(),
                price.text.strip(),
                location.text.strip(),
                f"https://www.olx.in{link['href']}"
            ])

print(f"Data saved to {filename}")