cols_to_add = [
    ("Url", "VARCHAR", 255),
    ("DatetimePosted", "DATETIME"),
    ("DaysSincePosted", "SMALLINT"),
    ("Latitude", "DOUBLE"),
    ("Longitude", "DOUBLE"),
    ("NumOfPics", "TINYINT"),
    ("Title", "VARCHAR", 255),
    ("Year", "YEAR"),
    ("Trim", "VARCHAR", 255),
    ("Fuel", "VARCHAR", 255),
    ("Odometer", "MEDIUMINT"),
    ("TitleStatus", "VARCHAR", 255),
    ("Transmission", "VARCHAR", 255),
    ("Cylinders", "TINYINT"),
    ("Drive", "VARCHAR", 255),
    ("PaintColor", "VARCHAR", 255),
    ("Size", "VARCHAR", 255),
    ("Type", "VARCHAR", 255),
    ("Price", "INT"),
    ("PostLength", "INT"),
    ("CLCity", "VARCHAR", 255),
    ("NumOfAttributes", "TINYINT"),
    ("CarCondition", "VARCHAR", 255),
    ("PostID", "BIGINT"),
    ("PostHistory", "VARCHAR", 1785),
    ("CarID", "BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY"),
    ("PriceHistory", "VARCHAR", 1785),
    ("make", "varchar", "255"),
    ("model", "varchar", "255"),
    ("website", "varchar", "255"),
    ("CarAge", "int"),
    ("DateUpdated", "datetime"),
    ("DaysSinceUpdated", "int")
]

# for col in cols_to_add:
#     if len(col) == 2:
#         MySQL.add_column("test_table", col[0], col[1])
#     if len(col) == 3:
#         MySQL.add_column("test_table", col[0], col[1], col[2])

# test_urls = [
#     "https://auburn.craigslist.org/cto/d/opelika-honda-civic-ex-5-speed/7037599414.html",
#     "https://bham.craigslist.org/cto/d/2009-honda-civic-ex-excellent-condition/7037604345.html",
#     "https://bham.craigslist.org/cto/d/birmingham-honda-civic-ex-2004/7037127289.html",
#     "https://bham.craigslist.org/cto/d/sulligent-2015-honda-civic-excellent/7035790246.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2008-honda-civic-lx/7034781445.html",
#     "https://bham.craigslist.org/cto/d/trussville-2003-honda-civic/7034619859.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2004-honda-civic-127k-miles/7033315128.html",
#     "https://bham.craigslist.org/cto/d/townley-2009-honda-civic/7031207759.html",
#     "https://bham.craigslist.org/cto/d/2009-honda-civic-ex-excellent-condition/7037604345.html",
#     "https://bham.craigslist.org/cto/d/alpine-2012-honda-civic-ex/7026987944.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2009-honda-civic-4-door/7023809829.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2015-honda-civic-lx-41k-miles/7023090671.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2008-honda-civic-lx/70347sfgwseGWSEGwesg8145.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/birmingham-2005-civic-coupe-stick-shift/7021399161.html",
#     "https://bham.craigslist.org/cto/d/bessemer-honda-civic-2014-price-drop/7019254017.html"
# ]


