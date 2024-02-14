import PyPDF2

pdfFileObj = open('python_tutorial.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print(len(pdfReader.pages))
pageObj = pdfReader.pages[18]
print(pageObj.extract_text())
pdfFileObj.close()
