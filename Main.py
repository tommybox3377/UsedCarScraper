from CLData import get_links_from_search, get_all_urls
import MySQL



urls = []
car_links = []

# urls.extend(get_all_urls())
# for url in urls:
#     get_links_from_search(url)
# print(len(car_links))

MySQL.add_column("honda_civic", "year", "YEAR")
