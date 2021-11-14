# Search "openpyxl.readthedocs"

# $ pip install openpyxl
from openpyxl import Workbook 
wb = Workbook() # Create a new workbook[excel file]
ws = wb.active # Get a curr activated worksheet in wb
ws.title = "NadoSheet"
wb.save("sample.xlsx") # This file is finally created in this dir
wb.close()