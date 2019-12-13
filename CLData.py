from bs4 import BeautifulSoup as bs
import re
import requests

ignore = []
urls = []
make = "honda"
model = "civic"
known_trims = ["si", "lx"]
owners = True
dealers = False
car_links = []


def get_all_urls():
    urls = []
    response = requests.get(r"https://www.craigslist.org/about/sites")
    content = response.content
    soup = bs(content, "html.parser")
    all_in_US = soup.find_all("div", {"class": "colmask"})[0]  # 0 index is just for how craigslist breaks up the urls by location
    for link in all_in_US.find_all('a'):
        urls.append(link.get('href'))

    return(urls)
    # --- this uses regex and is not as robust ---
    # soup = BeautifulSoup(response.text, "html.parser")
    # sites = soup.select("a[href^=\"https\"]")    #
    # for site in sites:
    #     x = re.search("https.*?\.org/", str(site))
    #     print(x[0])


def get_links_from_search(url):
    if owners and dealers:
        sold_by = "cta"
    elif owners:
        sold_by = "cto"
    elif dealers:
        sold_by = "ctd"
    else:
        return "Enter True for either or both owners/dealers vars"

    url_string = "%ssearch/%s?auto_make_model=%s+%s" % (url, sold_by, make, model)
    response = requests.get(url_string)
    content = response.content
    soup = bs(content, "html.parser")
    all = soup.find_all("li", {"class": "result-row"})
    for results in all:
        for link in results.find_all('a', {"class":"result-title hdrlnk"}):
            car_url = (link.get('href'))
            if url in car_url:
                print(car_url)
                car_links.append(car_url)
