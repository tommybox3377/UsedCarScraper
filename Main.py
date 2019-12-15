from CLData import get_all_urls, get_all_cl_cities_urls, first_search, check_if_listing_exists
import MySQL
from Cars import cars
import Logger

CraigsList = True
Carz = False  # Note it is cars.com but fro var naming reasons it is stored as Carz
Facebook = False


def retry_log_list():
    Logger.recycle_Urls()
    redo_urls = []
    MySQL.my_cursor.execute("SELECT url FROM urlstoscrape")
    data = MySQL.my_cursor.fetchall()
    for datum in data:
        redo_urls.append(datum[0])
    for url in redo_urls:
        MySQL.delete_entry("all_cars", "url", url)


def search_for_cars(car):
    if CraigsList:
        urls = []
        urls.extend(get_all_cl_cities_urls())
        for url in urls:
            get_all_urls(url, car.make, car.model)

        next_url = MySQL.get_next_url()
        while next_url:
            first_search(next_url, car)
            MySQL.delete_url(next_url)
            next_url = MySQL.get_next_url()


for car in cars:
    search_for_cars(car)
