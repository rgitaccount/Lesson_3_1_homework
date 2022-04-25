from bs4 import BeautifulSoup
import requests
import re


URL = "https://www.tenders.kg/Announcements_list.php?"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
}


def get_requests(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    items = soup.find_all("tr", class_="bs-gridrow")
    lots = []

    for item in items:
        lots.append(
            {
                "header": item.find("a").get_text().split(".")[0],
                "link": "https://www.tenders.kg/" + item.find("a").get("href"),
                "image": "https://www.tenders.kg/" + item.find("img").get("src"),
                "deadline": item.find("span", id=re.compile("_Deadline")).get_text()
            }
        )
    return lots


def scraper_script():
    html_text = get_requests(URL)
    if html_text.status_code == 200:
        lots = []
        for page in range(0, 3):
            html = get_requests(f"https://www.tenders.kg/Announcements_list.php?goto={page}")
            lots.extend(get_data(html.text))
        return lots
    else:
        raise Exception("Error in scraper script function")


if __name__ == "__main__":
    html_text = get_requests(URL)
    get_data(html_text.text)
    print(scraper_script())


