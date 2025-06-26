import scrapy


class HotelCard(scrapy.Item):
    name = scrapy.Field()
    city = scrapy.Field()
    neighborhood = scrapy.Field()
    address = scrapy.Field()
    stars = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    free_cancellation = scrapy.Field()
    property_url = scrapy.Field()