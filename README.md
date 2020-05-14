# os-scrapy-random-useragent

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
