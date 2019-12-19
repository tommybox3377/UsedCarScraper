from bs4 import BeautifulSoup as bs
import requests
import datetime
from urllib.parse import urlparse
import MySQL
import Logger
import re

ignore = []  # TODO optional add places to ignore then implement into get_all_cities
owners = True
dealers = False


def get_all_cl_cities_urls():
    urls = []
    response = requests.get(r"https://www.craigslist.org/about/sites")
    content = response.content
    soup = bs(content, "html.parser")
    all_in_US = soup.find_all("div", {"class": "colmask"})[0]  # 0 index is just for how craigslist breaks up the urls by location
    for link in all_in_US.find_all('a'):
        urls.append(link.get('href'))
    return urls


def get_all_urls(url, make, model):
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
        for link in results.find_all('a', {"class": "result-title hdrlnk"}):
            car_url = (link.get('href'))
            if url in car_url:
                print(car_url)
                MySQL.populate_table("urlstoscrape", ("url", car_url))


def first_search(url, car):
    if not check_if_listing_exists(url):
        return
    try:
        now = datetime.datetime.now()
        results = {
            "URL": url,
            "DatetimePosted": None,
            "DaysSincePosted": None,
            "Latitude": None,
            "Longitude": None,
            "NumOfPics": None,
            "CarCondition": None,
            "Title": None,
            "Year": None,
            "Trim": None,
            "Fuel": None,
            "Odometer": None,
            "TitleStatus": None,
            "Transmission": None,
            "Cylinders": None,
            "Drive": None,
            "PaintColor": None,
            "Size": None,
            "Type": None,
            "Price": None,
            "PostLength": None,
            "CLCity": urlparse(url)[1].split(".")[0],
            "NumOfAttributes": None,
            "PostID": None,
            "PriceHistory": None,
            "Make": car.make,
            "Model": car.model,
            "Website": "craigslist.org",
            "CarAge": None,
            "DateUpdated": None,
            "DaysSinceUpdated": None
        }
        response = requests.get(url)
        content = response.text
        soup = bs(content, "html.parser")

        info = soup.find_all("p", {"class": "postinginfo reveal"})
        for date in info:
            if "posted:" in date.get_text():
                results["DatetimePosted"] = datetime.datetime.strptime(date.find("time").get_text(), "%Y-%m-%d %H:%M")
                results["DaysSincePosted"] = (now - results["DatetimePosted"]).days
            elif "updated:" in date.get_text():
                results["DateUpdated"] = datetime.datetime.strptime(date.find("time").get_text(), "%Y-%m-%d %H:%M")
                results["DaysSinceUpdated"] = (now - results["DateUpdated"]).days

        info = soup.find("div", {"id": "map"})
        if info:
            results["Latitude"] = info.get("data-latitude")
            results["Longitude"] = info.get("data-longitude")

        info = soup.find("div", {"id": "thumbs"})
        if info:
            results["NumOfPics"] = len(info.find_all("a", {"class": "thumb"}))
        else:
            results["NumOfPics"] = 0

        try:
            info = soup.find_all("p", {"class": "attrgroup"})

            results["Title"] = (info[0].get_text().strip())
            atts = info[1].find_all("span")
            results["NumOfAttributes"] = len(atts)
            for att in atts:
                atr = att.contents[0]
                try:
                    val = att.find("b").get_text()
                except:
                    if "delivery available" not in atr.lower() and "cryptocurrency" not in atr.lower():
                        Logger.LogNote(f"attribute only had one index at {url}")
                if "condition" in atr:
                    results["CarCondition"] = val
                elif "fuel" in atr:
                    results["Fuel"] = val
                elif "odometer" in atr:
                    results["Odometer"] = val
                elif "title status" in atr:
                    results["TitleStatus"] = val
                elif "transmission" in atr:
                    results["Transmission"] = val
                elif "cylinders" in atr:
                    try:
                        results["Cylinders"] = re.search("\d+", val)[0]
                    except:
                        if "other" not in val:
                            Logger.LogError(f"could not read cylinders at {url}")
                elif "drive" in atr:
                    results["Drive"] = val
                elif "paint color" in atr:
                    results["PaintColor"] = val
                elif "size" in atr:
                    results["Size"] = val
                elif "type" in atr:
                    results["Type"] = val
                elif "vin" in atr.lower():
                    pass
                elif "delivery available" in atr.lower():
                    pass
                elif "cryptocurrency" in atr.lower():
                    pass
                else:
                    Logger.LogNote(f"Attribute {atr} was not found in dictionary for {url}")
        except Exception as e:
            Logger.LogNote("Attribute search error for " + url + str(e))

        info = soup.find("section", {"id": "postingbody"})
        if info:
            text = info.get_text()
            l = len(info.get_text())
            if "QR Code Link to This Post" in text:
                l -= 25
            results["PostLength"] = l

        info = soup.find("span", {"class": "price"})
        if info:
            price = re.search("\$*(\d+)", info.get_text())
            results["Price"] = (price[1])

        info = soup.find_all("p", {"class": "postinginfo"})
        for i in info:
            if "post id" in i.get_text():
                results["PostID"] = re.search("\d+", i.get_text())[0]

        if results["Title"]:
            title = results["Title"]
            results["Year"] = re.search("\d+", title)[0]
            #TODO check that year is in 4 digit format
            results["CarAge"] = now.year - int(results["Year"])

        if results["Price"]:
            results["PriceHistory"] = f"{now.strftime('%m/%d/%Y, %H:%M:%S')}${str(results['Price'])}"

        info = soup.find("span", {"id": "titletextonly"})
        for trim in car.trims:
            if re.search(f"[^a-z]{trim}[^a-z]*", info.get_text().lower()) or re.search(f"[^a-z]{trim}[^a-z]*", results["Title"]):
                results["Trim"] = trim
                break
    except Exception as e:
        Logger.LogCrash(f"{url} crashed during scraping of html response {str(e)}")

    for x, y in results.items():
        print(x, y)

    MySQL.populate_table_with_dict("test_table", results)


def update_car(url):
    # TODO there is an updated tag on CL next to the posted tag
    # new ones appear to noty have it though, maybe only updated ones?

    check_if_listing_exists(url)
    response = requests.get(r"https://www.craigslist.org/about/sites")
    content = response.content
    soup = bs(content, "html.parser")


def check_if_listing_exists(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            if response.status_code == 404:
                Logger.LogNote(f"{url} had a 404 response code")
            else:
                Logger.LogError(f"{url} did not have a 200 response code")
            return False
        if "This posting has been flagged for removal." in response.text:
            Logger.LogNote(f"{url} was flagged for removal")
            return False
        if "This posting has expired" in response.text:
            Logger.LogNote(f"{url} has expired")
            return False
        if "This posting has been deleted by its author." in response.text:
            Logger.LogNote(f"{url} has been deleted by its author")
            return False
        return True
    except:
        Logger.LogError(f"{url} failed try block in check_listing_exists")
        return False


# TODO when inputing/parsing all data, check that it is within range of MySQL datatype
