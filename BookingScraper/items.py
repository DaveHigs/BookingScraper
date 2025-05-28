import scrapy


class HotelCard(scrapy.Item):
    name = scrapy.Field()
    stars = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()