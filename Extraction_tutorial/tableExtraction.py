import tabula
import pandas as pd
from PyPDF2 import PdfReader
from pdfminer.high_level import extract_text
import pdfplumber

path = '../2023ssis-16-49-1.pdf'

def extract_tables_from_pdf(file_path):
    # Accepts file path as an argument
    tables = tabula.read_pdf(file_path, pages='all', multiple_tables=True)
    # Extract tables from PDF document using tabula library
    dataframes = []
    for table in tables:
        df = pd.DataFrame(table)
        dataframes.append(df)
    return dataframes

if __name__ == '__main__':
    print()
    print("=" * 100)
    print("tabular-py")
    print("=" * 100)
    dataframes = extract_tables_from_pdf(path)
    for i, df in enumerate(dataframes):
        print(f'Table {i+1}:')
        print(df)

    # # fitz
    # # print()
    # # print("=" * 100)
    # # print("fitz")
    # # print("=" * 100)
    # # doc = fitz.open(path)
    # # for page in doc:
    # #     text = page.get_text()
    # #     print(text)

    # pypdf2
    print()
    print("=" * 100)
    print("pypdf2")
    print("=" * 100)
    reader = PdfReader(path)
    pages = reader.pages
    text = ""
    for page in pages:
        sub = page.extract_text()
        text += sub
    print(text)

    # # pdfminer
    # print()
    # print("=" * 100)
    # print("pdfminer")
    # print("=" * 100)
    # text = extract_text(path)
    # print(text)

    # # pdfplumber
    # print()
    # print("=" * 100)
    # print("pdfplumber")
    # print("=" * 100)
    # pdf = pdfplumber.open(path)
    # pages = pdf.pages
    # text = ""
    # for page in pages:
    #     sub = page.extract_text()
    #     text += sub
    # print(text)