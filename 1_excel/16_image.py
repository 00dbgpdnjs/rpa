from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.workbook.workbook import Workbook
wb = Workbook()
ws = wb.active

img = Image("img.png")

ws.add_image(img, "C3")

wb.save("sample_image.xlsx")

# ImportError : You must imstall Pillow to fetch image...
# $ pip install Pillow