from NaverNewsCrawler import NaverNewsCrawler


def main():
    keyword = input('원하는 키워드를 입력하세요: ')
    crawler = NaverNewsCrawler(keyword)
    file_name = input('저장할 파일명을 입력하세요: ')
    crawler.get_news(file_name)


if __name__ == '__main__':
    main()
