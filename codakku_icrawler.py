from icrawler.builtin import GoogleImageCrawler
crawler = GoogleImageCrawler(storage={"root_dir": 'codakku'})
crawler.crawl(keyword='コダック', max_num=10)
