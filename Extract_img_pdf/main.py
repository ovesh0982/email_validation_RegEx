print("How To Extract Images From PDF")

import pikepdf
'''
# 1. Reading a PDF File
# Yeh example ek PDF file ko read karta hai aur pages ki ginti dikhata hai:

pdf = pikepdf.open('C:/Users/DESKTOP/Desktop/python/Extract_img_pdf/pdf1.pdf')
print(f"Number of pages: {len(pdf.pages)}")
'''


# 2. Splitting a PDF File
# Ek PDF file ko split karne ka example:
pdf = pikepdf.open('C:/Users/DESKTOP/Desktop/python/Extract_img_pdf/pdf1.pdf')

for i,page in enumerate(pdf.pages):
  new_pdf = pikepdf.Pdf.new()
  new_pdf.pages.append(page)
  new_pdf.save(f'page_{i+1}.pdf')
  new_pdf.close()

pdf.close()