import json
import openpyxl

wb = openpyxl.load_workbook('products.xlsx')
sheet = wb['Sheet1']
products = {}
for row in sheet.iter_rows(min_row=2, max_row=7, min_col=1, max_col=4, values_only=True):
    product_id = row[0]
    product = {
        "name": row[1],
        "price": row[2],
        "available": row[3]
    }
    products[product_id] = product
print(json.dumps(products, indent=4))
