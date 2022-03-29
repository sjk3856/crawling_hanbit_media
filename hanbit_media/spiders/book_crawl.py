import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookCrawlSpider(CrawlSpider):
    #클롤러 이름
    name = 'book_crawl'

    #크롤러 실행을 허용할 도메인
    allowed_domains = ['hanbit.co.kr/']

    #시작점으로 사용한 URL
    #리스트로 지정해 한 번에 여러 웹 페이지에서 크롤링을 시작하게 할 수 있음.
    start_urls = ['http://www.hanbit.co.kr/',
    'https://www.hanbit.co.kr/store/books/category_list.html?cate_cd=001',
    'https://www.hanbit.co.kr/store/books/category_list.html?cate_cd=002',
    'https://www.hanbit.co.kr/store/books/category_list.html?cate_cd=003',
    'https://www.hanbit.co.kr/store/books/category_list.html?cate_cd=004',
    'https://www.hanbit.co.kr/store/books/category_list.html?cate_cd=005',
    'https://www.hanbit.co.kr/store/books/category_list.html?cate_cd=006',
    'https://www.hanbit.co.kr/store/books/category_list.html?cate_cd=007',
    'https://www.hanbit.co.kr/store/books/category_list.html?cate_cd=008',]

    #클롤러가 어떻게 작동할지 규칙을 설정
    #크롤러는 시작점의 모든 링크를 검사한 후 규칙에 맞는 링크가 있으면 정해진 콜백 메서드를 실행함.
    #follow가 True이면 해당 페이지의 링크를 대상으로 재귀적으로 앞 작업을 반복함.
    #규칙은 여러 개를 만들 수 있다.
    rules = (
        Rule(LinkExtractor(allow=r'store/books/liik.php\?p_code=.*'),
        callback='parse_item',
        follow=True),

        Rule(LinkExtractor(allow=
        r'store/books/category_list\.html\?page=\d+&cate_cd=00\d+&str=p_pub_date'))
    )

    #rules를 통과한 링크에 요청을 보내 응답을 받으면 Rule()에 설정한 콜백 메서드를 해당 응답 결과에 실행함.
    #response를 파라미터로 받고 XPath, CSS 선택자를 이용해서 원하는 요소를 추출함.
    def parse_item(self, response):
        i = {}
        i['book_title'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[1]/text()').extract()
        i['book_author'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[1]/ul/li[strong/text()="저자 : "]/span/text()').extract()
        i['book_translator'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[1]//ul/li[strong/text()="번역 : "]/span/text()').extract()
        i['book_pub_date'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[1]//ul/li[strong/text()="출간 : "]/span/text()').extract()
        i['book_isbn'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[1]//ul/li[strong/text()="ISBN : "]/span/text()').extract()
        return i

    
