import scrapy
from scrapy_playwright.page import PageMethod

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

    async def parse(self, response):
        page = response.meta['playwright_page']

        for i in range (5):
            await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
            await page.wait_for_timeout(2000)

        await page.screenshot(path='./screenshot.png', full_page=True)
        await page.close()