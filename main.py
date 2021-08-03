from NaverNewsCrawler import NaverNewsCrawler
from openpyxl import load_workbook


def main():
    keyword = input('원하는 키워드를 입력하세요: ')
    crawler = NaverNewsCrawler(keyword)
    file_name = input('저장할 파일명을 입력하세요: ')
    crawler.get_news(file_name)


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


if __name__ == '__main__':
    main()
