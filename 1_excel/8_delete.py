from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# Student #6 transfers school so erase that line.
ws.delete_rows(8)
# ws.delete_rows(8,3) # (from where, how many)

# ws.delete_cols(2) # Delete B열[all 영어점수] 

wb.save("sample_delete_row.xlsx")