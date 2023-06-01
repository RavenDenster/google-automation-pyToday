from icrawler.builtin import GoogleImageCrawler

def google_img_downloader():
    filters = dict(
        type='photo',
        color='blackandwhite',
        size='large', # icon, ==224x224
        # license='noncommercial, commercial',
        # date = ((2020, 1, 1), (2023, 5, 14))
    )
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})

    # crawler.crawl(keyword='Torufin Vinland Saga', max_num=3)
    # crawler.crawl(keyword='Mitsuri Demon Slayer', max_num=3, min_size=(700, 700),  overwrite=True) # overwrite перезаписывает старые изображения по этому же запросу
    # crawler.crawl(keyword='Czech', max_num=3, min_size=(700, 700),  overwrite=True, filters=filters, file_idx_offset='auto')
    # crawler.crawl(keyword='New York', max_num=3, min_size=(1000, 1000),  overwrite=True, filters=filters, file_idx_offset='auto')
    crawler.crawl(keyword='Spider', max_num=1, filters=filters, file_idx_offset='auto')

def main():
    google_img_downloader()

if __name__ == '__main__':
    main()