from NaverNewsCrawler import NaverNewsCrawler
from openpyxl import load_workbook
from sending_email import send_mail
import os


def main():
    keyword = input('원하는 키워드를 입력하세요: ')
    crawler = NaverNewsCrawler(keyword)
    file_name = input('저장할 파일명을 입력하세요(현재 경로 아니라면 경로 포함): ')
    crawler.get_news(file_name)

    # 이메일 확인
    addrs = get_addrs()
    contents = '안녕하세요. 네이버에서 기사 크롤링 한거 엑셀 파일로 보내드립니다.'
    for addr in addrs:
        name, email = addr
        send_mail(name, email, '기사 크롤링입니다.', contents, file_name)


def get_addrs():
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


def validate_excel(file_name):


if __name__ == '__main__':
    main()
