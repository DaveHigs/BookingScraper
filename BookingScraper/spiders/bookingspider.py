import scrapy
from BookingScraper.items import HotelCard

class BookingSpider(scrapy.Spider):
    name = 'Booking'
    start_urls = [
        'https://www.booking.com/searchresults.html?ss=Barcelona&dest_id=-372490&dest_type=city&checkin=2025-08-11&checkout=2025-08-17&group_adults=2&no_rooms=1&group_children=0&lang=en-us&soz=1&lang_changed=1&selected_currency=EUR'
    ]

    def start_requests(self):
        url = self.start_urls[0]
        yield scrapy.Request(url, 
                             meta={'playwright': True,
                                    "playwright_include_page": True}
                             , callback=self.parse)

    def __init__(self):
        self.hotel_urls = []
    
    async def parse(self, response):
        page = response.meta['playwright_page']

        for i in range(10):
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            await page.wait_for_timeout(8000)

            load_more_button = page.get_by_role('button', name='Load more results')

            if await load_more_button.is_visible():
                await load_more_button.click()
                await page.wait_for_timeout(8000)
            else:
                break

        content = await page.content()
        await page.close()
        
        response = response.replace(body=content)
        property_cards = response.css('div.aa97d6032f')

        for card in property_cards:
            hotel = HotelCard()
            hotel['name'] = card.css('div.b87c397a13::text').get()
            hotel['neighborhood'], hotel['city'] = card.css('span.d823fbbeed::text').get().split(', ')
            hotel['stars'] = card.css('div.ebc566407a::attr(aria-label)').get()[0]
            hotel['rating'] = card.css('div.f63b14ab7a::text').get()
            raw_price = card.css('span.b87c397a13::text').get()
            clean_price = raw_price.replace('\xa0', '').replace('€', '').replace(',', '')
            hotel['price'] = clean_price
            hotel['currency'] = 'EUR'
            hotel['free_cancellation'] = True if card.css('div.fff1944c52').get() else False
            full_url = card.css('a::attr(href)').get()
            hotel['property_url'] = full_url

            yield scrapy.Request(url=full_url, callback=self.parse_details, meta={'hotel': hotel})


        count = len(property_cards)
        self.logger.info(f'Amount of property cards scraped: {count}')

    def parse_details(self, response):
        hotel = response.meta['hotel']

        hotel['address'] = response.css('div.b99b6ef58f::text').get()

        yield hotel
