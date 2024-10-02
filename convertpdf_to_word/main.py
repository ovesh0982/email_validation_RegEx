print("Convert PDF to WORD & WORD to PDF")
'''
importan notes: pdf2docx ka use-
pdf2docx library Python mein PDF files ko Microsoft Word (DOCX) format mein convert karne ke liye use hoti hai. Is library ki madad se aap PDF documents ko editable Word documents mein badal sakte hain, jo ki aapko text, images, aur formatting ko edit karne ki suvidha deti hai.
'''

from pdf2docx import Converter
old_pdf = "C:/Users/DESKTOP/Desktop/python/convertpdf_to_word/Ovesh_Sir_Resume1.pdf"
new_doc = "new.dock"

obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()
