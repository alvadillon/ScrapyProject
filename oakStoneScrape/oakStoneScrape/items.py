# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class OakstonescrapeItem(scrapy.Item):
    # define the fields for your item here like:
     course_title = scrapy.Field()
     learning_objectives = scrapy.Field()
     last_course_update = scrapy.Field()
     original_release = scrapy.Field()
     date_credits_expire = scrapy.Field()
     intended_audience = scrapy.Field()
     course_overview = scrapy.Field()
     online_course_price = scrapy.Field()
     accreditation = scrapy.Field()
     course_topics = scrapy.Field()
     course_subtopics = scrapy.Field()
     course_subtopic_instructors = scrapy.Field()




