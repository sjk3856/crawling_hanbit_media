import scrapy


class HanbitMediaItem(scrapy.Item):
    # define the fields for your item here like:
    
    #책 이름
    book_title = scrapy.Field()

    #저자 이름
    book_author = scrapy.Field()

    #반역자 이름
    book_translator = scrapy.Field()

    #출간일
    book_pub_date = scrapy.Field()

    #ISBN
    book_isbn = scrapy.Field()
    pass
