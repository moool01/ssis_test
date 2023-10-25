""" dependency : pypdf. """

class Extract_Text_From_PDF() :
    def __init__(self, file) :
        """ Get File From Local and Wrap with pypdf.PdfReader. """

        try : import pypdf
        except ImportError :      
            print(""" Error Occured. Try pip install pypdf. """)
            exit(0)

        self.file = pypdf.PdfReader(file)

    def extract_text(self, start_page=1, end_page=None, path="./result.txt") :
        """ 객체에 추출한 텍스트 담아서 path에 지정된 파일에 저장. start page부터 end page까지. """

        text = ""

        for i in range(start_page-1, end_page+1) :
            text += f'\n============================================================\nStart of Page {i+1}.\n============================================================\n\n'
            text += self.file.pages[i].extract_text()
            text += f'\n\n============================================================\nEnd of Page {i+1}.\n============================================================\n'

        with open(path, "w", encoding='utf-8') as file :
            file.write(text)
        
if __name__ == "__main__" :
    extract = Extract_Text_From_PDF(file="document.pdf")
    start_page = int(input("Enter Start Page : "))
    end_page = int(input("Enter End Page : "))
    extract.extract_text(start_page=start_page, end_page=end_page)

    print("\n Extraction Complete. End of Script.")
