from PyPDF2 import PdfReader
import re
import csv

# 정규 표현식 패턴
pattern = r'\|([^|]+)\|'

# 예제 PDF 파일 경로
# PDF_FILE_PATH = "../2023_guide_total.pdf" # 기존 파일
PDF_FILE_PATH = "../2023ssis-16-49.pdf" # 잘라둔 파일

reader = PdfReader(PDF_FILE_PATH)
pages = reader.pages
text = ""
for page in pages:
    sub = page.extract_text()
    text += sub
print('print : pdf text')
print('-' * 20)
print(text)
print('-' * 20)

lines = []
for i in range(len(pages)):
    lines += pages[i].extract_text().split('\n')

# 결과를 저장할 리스트 초기화
result_list = []

# 현재 주제에 대한 정보를 저장할 딕셔너리 초기화
current_dict = {'제목': '', '대상': '', '내용': '', '방법': '', '문의': ''}
current_subtitle = None

# 페이지 내용 처리
for line in lines:
    # 각 라인을 분석하고 소제목과 내용을 채움
    if "|" in line:
        # 정규 표현식과 매치
        match = re.search(pattern, line)
        # 매치된 결과 가져오기
        if match:
            captured_text = match.group(1).strip()  # 매치된 결과의 앞뒤 공백 제거
            if not captured_text.startswith('제'):
                # 이전 주제에 대한 정보가 있다면 결과 리스트에 추가
                if current_dict['제목']:
                    result_list.append(current_dict)
                    # 현재 주제에 대한 정보를 저장할 딕셔너리 초기화
                    current_dict = {'제목': '', '대상': '', '내용': '', '방법': '', '문의': ''}
                current_dict['제목'] = line
    elif line.startswith(" 대상"):
        current_subtitle = '대상'
        current_dict[current_subtitle] = line
    elif line.startswith(" 내용"):
        current_subtitle = '내용'
        current_dict[current_subtitle] = line
    elif line.startswith(" 방법"):
        current_subtitle = '방법'
        current_dict[current_subtitle] = line
    elif line.startswith(" 문의"):
        current_subtitle = '문의'
        current_dict[current_subtitle] = line
    else:
        # 현재 소제목에 내용 추가
        if current_subtitle:
            current_dict[current_subtitle] += '\n' + line

# 마지막 주제에 대한 정보 추가
if current_dict['제목']:
    result_list.append(current_dict)

# CSV 파일로 저장
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['제목', '대상', '내용', '방법', '문의']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

    # CSV 헤더 작성
    writer.writeheader()

    # 각 딕셔너리를 CSV 로우로 저장
    for entry in result_list:
        writer.writerow(entry)

