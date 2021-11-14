from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# Move English and math to the side.
ws.move_range("B1:C11", rows=0, cols=1)
ws["B1"].value = "국어"

wb.save("sample_korean.xlsx")