import PyPDF2

def add_watermark(water_file, page_obj):
    file = open(water_file, 'rb')
    pdf_reader = PyPDF2.PdfReader(file)
    page_obj.merge_page(pdf_reader.pages[0])

    return page_obj


def main():
    pdf_file = open('example.pdf', 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_writer = PyPDF2.PdfWriter()

    for page in range(len(pdf_reader.pages)):
        page_watermark = add_watermark('watermark.pdf', pdf_reader.pages[page])
        pdf_writer.add_page(page_watermark)

    f = open('watermarked_example.pdf','wb')
    pdf_writer.write(f)


if __name__ == "__main__":
    main()