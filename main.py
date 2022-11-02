import os
from PyPDF2 import PdfFileMerger

pdf = PdfFileMerger(strict=False)

for file in os.listdir():
    if file.endswith(".pdf"):
        pdf.append(file)

pdf.write("Merged.pdf")
pdf.close()
print("Merged successfully")
