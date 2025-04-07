import scrapy

class BookingSpider(scrapy.Spider):
    name = 'Booking'
    start_urls = [
        'https://www.booking.com/searchresults.html?ss=Barcelona&dest_id=-372490&dest_type=city&checkin=2025-08-11&checkout=2025-08-17&group_adults=2&no_rooms=1&group_children=0&lang=en-us&soz=1&lang_changed=1&selected_currency=EUR'
    ]

