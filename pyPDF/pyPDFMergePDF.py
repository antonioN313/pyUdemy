import PyPDF2


def pdf_merge(pdfs, output):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdfs:
        pdf_merger.append(pdf)

    with open(output, 'wb') as f:
        pdf_merger.write(f)


def main():
    pdfs = ['example.pdf', 'rotated_example.pdf']
    output = 'merged_example.pdf'
    pdf_merge(pdfs, output)


if __name__ == "__main__":
    main()
