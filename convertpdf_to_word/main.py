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

'''
imp:- libraries ke andar ke function

1. Converter Class
Yeh class PDF file ko DOCX mein convert karne ke liye use hoti hai.

2. Page Class
Yeh class individual pages ko represent karti hai.


3. Text Extraction Functions
Kuch internal functions hain jo PDF se text extract karne mein madad karte hain. Yeh functions automatically call hote hain jab aap convert method call karte hain.

4. Image Handling
pdf2docx images ko bhi extract karta hai aur unhe DOCX mein include karta hai. Yeh internal functions ke through hota hai.
'''