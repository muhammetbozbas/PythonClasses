from csv import DictWriter, DictReader

# with open("products.csv","w") as file:
#     headers = ["ProductName","Price","IsPublished","Category","Reviews"]
#     csv_writer = DictWriter(file, headers)
#     csv_writer.writeheader() #başlık yazdırmak için
#     csv_writer.writerows([
#         {
#             "ProductName": "IPhone 7",
#             "Price": "7000",
#             "IsPublished": True,
#             "Category" : "Telefon",
#             "Reviews": 4.7
#         },
#         {
#             "ProductName": "IPhone 8",
#             "Price": "1100",
#             "IsPublished": True,
#             "Category" : "Telefon",
#             "Reviews": 4.7
#         }, 
#         {
#             "ProductName": "IPhone 13",
#             "Price": "31100",
#             "IsPublished": True,
#             "Category" : "Telefon",
#             "Reviews": 4.7
#         }])

"""
#appending
with open("products.csv","a") as file:
    headers = ["ProductName","Price","IsPublished","Category","Reviews"]
    csv_writer = DictWriter(file, headers)
    csv_writer.writerow(
        {
            "ProductName": "IPhone 13",
            "Price": "31000",
            "IsPublished": True,
            "Category" : "Telefon",
            "Reviews": 4.7
        },
        )
"""


def price_with_tax(price):
    return float(price)* 1.18


with open("products.csv") as file:
    csv_reader = DictReader(file)
    products = list(csv_reader)
    


with open("new-products.csv","w") as file:
    headers = ["ProductName","Price","IsPublished","Category","Reviews"]
    csv_writer = DictWriter(file, headers)
    csv_writer.writeheader() #başlık yazdırmak için
    for p in products:
        csv_writer.writerow({
                "ProductName": p["ProductName"],
                "Price": price_with_tax(p["Price"]),  #price with tax
                "IsPublished": p["IsPublished"],
                "Category" : p["Category"],
                "Reviews": p["Reviews"]
            })