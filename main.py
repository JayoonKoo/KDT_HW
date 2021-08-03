from NaverNewsCrawler import NaverNewsCrawler
from openpyxl import load_workbook
from sending_email import send_mail
import os


def main():
    # keyword 받고 .xlsx로 저장
    keyword, file_name = '', ''
    while(not keyword or not file_name):
        keyword = input('원하는 키워드를 입력하세요: ')
        file_name = input('저장할 파일명을 입력하세요(현재 경로 아니라면 경로 포함): ')
    file_name = set_filename(file_name)
    crawler = NaverNewsCrawler(keyword)
    crawler.get_news(file_name)

    # 이메일 확인
    addrs = get_addrs()
    contents = '안녕하세요. 네이버에서 기사 크롤링 한거 엑셀 파일로 보내드립니다.'
    for addr in addrs:
        name, email = addr
        send_mail(name, email, '기사 크롤링입니다.', contents, file_name)


def get_addrs():
    """
    엑셀에서 메일 보내야할 주소를 읽어서 addrs 반환하는 함수
    Returns:
        addrs
    """
    wb = load_workbook('email list_fastcampus news.xlsx')
    data = wb.active
    area = data['B3:C4']

    addrs = []
    for row in area:
        addr = []
        for cell in row:
            addr.append(cell.value)
        addrs.append(addr)

    return addrs


def set_filename(file_name):
    """
    file_name 검증 후 엑셀 파일 확장자로 수정하는 함수

    Args: 
        file_name: 사용자로 부터 입력받은 파일 형식

    Returns:
        file_name: 파일 형식 변경 후 리턴
    """
    name, ext = os.path.splitext(file_name)
    if not ext == '.xlsx':
        file_name = f'{name}.xlsx'
    return file_name


if __name__ == '__main__':
    main()
