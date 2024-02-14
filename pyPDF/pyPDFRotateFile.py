import PyPDF2


def pdf_rotate(origin_file_name, new_file_name, rotation):
    pdf_file = open(origin_file_name,'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_writer = PyPDF2.PdfWriter()

    for page in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page]
        page_obj.rotate(rotation)
        pdf_writer.add_page(page_obj)

    new_file = open(new_file_name, 'wb')
    pdf_writer.write(new_file)
    pdf_file.close()
    new_file.close()


def main():
    pdf_rotate('example.pdf', 'rotated_example.pdf', 180)


if __name__ == "__main__":
    main()


