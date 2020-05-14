# os-scrapy-random-useragent

[![Build Status](https://www.travis-ci.org/cfhamlet/os-scrapy-random-useragent.svg?branch=master)](https://www.travis-ci.org/cfhamlet/os-scrapy-random-useragent)
[![codecov](https://codecov.io/gh/cfhamlet/os-scrapy-random-useragent/branch/master/graph/badge.svg)](https://codecov.io/gh/cfhamlet/os-scrapy-random-useragent)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/os-scrapy-random-useragent.svg)](https://pypi.python.org/pypi/os-scrapy-random-useragent)
[![PyPI](https://img.shields.io/pypi/v/os-scrapy-random-useragent.svg)](https://pypi.python.org/pypi/os-scrapy-random-useragent)

This project provide a [Downloader Middleware](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html) to change 'User-Agent' of request headers.


## Install

```
pip install os-scrapy-random-useragent
```

## Usage

### Settings

* enable downloader middleware in settings.py file:


    this middleware will override default Scrapy User-Agent


    ```
    DOWNLOADER_MIDDLEWARES = {
        "os_scrapy_random_useragent.RandomUserAgentMiddleware": 543,
    }
    
    ```

* config useragents:
   
    - by file:

        ```
        USER_AGENTS = "./your-useragets-file"
        ```

    - by string:

        ```
        USER_AGENTS = "Your-Useragent-String"
        ```

    - by list:

        ```
        USER_AGENTS = ["User-Agent-01", "User-Agent-02"]
        ```

## Unit Tests

```
tox
```

## License

MIT licensed.
