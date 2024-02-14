import PyPDF2

f = open('example.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
pdf_writer = PyPDF2.PdfWriter()

for page in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page])

pdf_writer.encrypt('la-li-lu-le-lo')
result_pdf = open('Protected_Example.pdf', 'wb')
pdf_writer.write(result_pdf)
print(pdf_reader.is_encrypted)
#pdf_writer.decrypt('la-li-lu-le-lo')
