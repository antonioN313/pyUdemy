import openpyxl

wb = openpyxl.load_workbook('sales.xlsx')
sheet = wb.active
sheet.delete_cols(1)
sheet.delete_rows(4)
sheet.insert_cols(2)
wb.save('sales_mod.xlsx')
