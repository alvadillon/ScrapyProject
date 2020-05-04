import scrapy
from ..items import OakstonescrapeItem

class CourseSpider(scrapy.Spider):
    name = "course-info"
    start_urls = [
        "https://www.oakstone.com/electrodiagnostic-medicine-and-neuromuscular-disorders-a-comprehensive-review"
        ]

    def parse(self, response):

        items = OakstonescrapeItem()

        course_title = response.css("h1::text")[0].extract()
        learning_objectives = response.xpath("//div[@id='tab-accreditation']//li/text()").extract()
        last_course_update = response.xpath("//div[@id='tab-accreditation']//p[4]/text()")[0].extract()
        original_release = response.xpath("//div[@id='tab-accreditation']//p[4]/text()")[2].extract()
        date_credits_expire = response.xpath("//div[@id='tab-accreditation']//p[4]/text()")[4].extract()
        intended_audience = response.xpath("//p[contains(text(),'This educational activity')]/text()").extract()
        course_overview = response.xpath("//div[@id='overview-left']//li/text()").extract()
        online_course_price = response.css("span.price-val-for-dyn-upd-2714::text").extract()
        accreditation = response.xpath("//p[contains(text(),'accredited')]/text()").extract()
        course_topics = response.xpath('//div[@id="tab-speaker"]//div[@class="container"]//h3/text()').extract()
        course_subtopics = response.xpath('//div[@id="tab-speaker"]//div[@class="container"]//li/text()').extract()
        course_subtopic_instructors = response.xpath('//div[@id="tab-speaker"]//div[@class="container"]//em/text()').extract()
        
        items['course_title'] = course_title
        items['learning_objectives'] = learning_objectives
        items['last_course_update'] = last_course_update
        items['original_release'] = original_release
        items['date_credits_expire'] = date_credits_expire
        items['intended_audience'] = intended_audience
        items['course_overview'] = course_overview
        items['online_course_price'] = online_course_price
        items['accreditation'] = accreditation
        items['course_topics'] =  course_topics
        items['course_subtopics'] = course_subtopics
        items['course_subtopic_instructors'] = course_subtopic_instructors
        yield items
       
