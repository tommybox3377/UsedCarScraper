# import MySQL
# import random
#
#
#
# # MySQL.add_column("largedata", "datDAM", "LONGBLOB")
# # for i in range(500):
# #     x = random.randint(100000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000)
# #     y = random.randint(100000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000)
# #     z = random.randint(100000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000)
# #
# #     blob = str(x * y * z)
# #     while len(blob) < 3000000:
# #         blob += blob
# #     else:
# #         print(len(str(blob)))
# #         print("test")
# #         filename = str(random.randint(10000000, 100000000)) + ".dat"
# #         MySQL.populate_table("largedata", ("FileName", f"{filename}"), ("datDAM", blob))
#
# MySQL.my_cursor.execute(f"SELECT datDAM FROM largedata WHERE FileName Like '%2.dat'")
#
# datum = MySQL.my_cursor.fetchall()
#
# for dat in datum:
#     print(len(dat[0]))
#

