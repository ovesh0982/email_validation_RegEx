import PyPDF2

# Merging PDF files
pdf_files = ['pdf1.pdf', 'pdf2.pdf',]  # aapke PDF files ke naam yahan
merger = PyPDF2.PdfWriter()

for pdf in pdf_files:
    merger.append(pdf)

# Merged file ka naam
merger.write('merged.pdf')
merger.close()

print("PDF files merged successfully!")
