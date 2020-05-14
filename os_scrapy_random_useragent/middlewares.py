# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import os
import random

from scrapy import signals
from scrapy.exceptions import NotConfigured


class OsScrapyRandomUseragentSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class OsScrapyRandomUseragentDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


def bytes_to_text(s):
    if isinstance(s, bytes):
        return s.decode("utf-8")
    return s


class RandomUserAgentMiddleware(object):
    def __init__(self, crawler):
        self.crawler = crawler
        self.ua_list = []
        self.default_useragent = bytes_to_text(crawler.settings.get("USER_AGENT"))
        try:
            self.load()
        except Exception as e:
            raise NotConfigured(f"load fail {e}")

    def process_request(self, request, spider):
        request_useragent = request.headers.get("User-Agent", None)
        if (
            not request_useragent
            or bytes_to_text(request_useragent) == self.default_useragent
        ):
            ua = random.choice(self.ua_list)
            request.headers.setlist(b"User-Agent", ua)

    def load(self):
        u = self.crawler.settings.get("USER_AGENTS")
        if isinstance(u, list):
            uas = [x.strip() for x in u if len(x.strip()) > 0]
            if len(uas) <= 0:
                raise Exception("no available useragent")
            self.ua_list = uas
            return
        elif isinstance(u, str):
            u = u.strip()
            if os.path.isfile(u):
                with open(u, "r") as f:
                    uas = [x.strip() for x in f.readlines() if len(x.strip()) > 0]
                    if len(uas) <= 0:
                        raise Exception(f"no useragent in file {u}")
                    self.ua_list = uas
            else:
                if len(u) <= 0:
                    raise Exception(f"empty string")
                self.ua_list = [u]
            return
        raise Exception(f"invalid USER_AGENTS {u}")

    @classmethod
    def from_crawler(cls, crawler):
        if crawler.settings.get("USER_AGENTS", None) is None:
            raise NotConfigured("not set USER_AGENTS")
        return cls(crawler)
