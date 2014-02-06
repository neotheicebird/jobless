#!/usr/bin/env python
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from jobfeed.items import JobFeedItem

class JobFeedSpider(CrawlSpider):

    name = 'jobfeed'
    allowed_domains = ['elance.com']
    keywords = ['scrapy', 'python', 'matlab']
    start_urls = ['https://www.elance.com/r/jobs/q-%s' % keyword for keyword in keywords]
#    tokens = ['q-%s' % keyword for keyword in keywords]
    rules = [Rule(SgmlLinkExtractor(allow=''), 'parse_jobs')]

    def parse_jobs(self, response):
        """Parses each job listing and returns a list of items"""
        sel = Selector(response)
        jobCards = sel.xpath("//div[@id='eol-container']/div[@id='eol-bd']"
                         "/div[@class='eol-center search-layout']"
                         "/div[@class='search-layout-right']"
                         "/div[@id='jobSearchResults']"
                         "/div[@class='jobCard']"
                        )
        jobs = []
        for card in jobCards:
            job = JobFeedItem()
            job['title'] = card.xpath("div/a[@class='title']/text()").extract()
            job['link'] = card.xpath("div/a").re("""\s*(?i)href\s*=\s*(\"([^"]*\")|'[^']*'|([^'">\s]+))""")
            job['description'] = card.xpath("div[@class='desc']/text()").extract()
            job['price'] = card.xpath("div[@class='stats']/span[@class='bold']/text()").extract() # e.g 'Hourly Rate: 15$/hr'

            stats = card.xpath("div[@class='stats']/text()").re('[^|\xa0]+')
            posted = ''
            ends = ''
            for line in stats:
                if 'Posted' in line:
                    posted = line
                if 'Ends' in line:
                    ends = line

            job['posted'] = posted
            job['ends'] = ends

            jobs.append(job)
        return jobs

        #sel.xpath("//div[@id='eol-container']").xpath("div[@id='eol-bd']")
        #.xpath("div[@class='eol-center search-layout']")
        #.xpath("div[@class='search-layout-right']")
        #.xpath("div[@id='jobSearchResults']")
        #.xpath("div[@class='jobCard']").extract()


        #sel.xpath("//div[@id='eol-container']").xpath("div[@id='eol-bd']")
        #.xpath("div[@class='eol-center search-layout']")
        #.xpath("div[@class='search-layout-right']")
        #.xpath("div[@id='jobSearchResults']")
        #.xpath("div[@class='jobCard']")
        #.xpath("div/a").re("""\s*(?i)href\s*=\s*(\"([^"]*\")|'[^']*'|([^'">\s]+))""")

