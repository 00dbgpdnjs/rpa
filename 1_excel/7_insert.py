from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # Insert a blank line at the 8th row
ws.insert_rows(8, 5) # (from where, how many)

# ws.insert_cols(2)
# ws.insert_cols(2, 3)

wb.save("sample_insert_rows.xlsx")