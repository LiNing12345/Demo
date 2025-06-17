import scrapy
import json
from Demo.items import DemoItem

class NikeSpider(scrapy.Spider):
    name = "nike"
    # allowed_domains = ["nike.com"]
    start_urls = [
        'https://api.nike.com.cn/cic/browse/v2?queryid=products&anonymousId=DSWX092BF0B906D9ED416BC37EAACD002AC2&country=cn&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(CN)%26filter%3Dlanguage(zh-Hans)%26filter%3DemployeePrice(true)%26anchor%3D0%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=zh-Hans&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D',
        'https://api.nike.com.cn/cic/browse/v2?queryid=products&anonymousId=DSWX092BF0B906D9ED416BC37EAACD002AC2&country=cn&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(CN)%26filter%3Dlanguage(zh-Hans)%26filter%3DemployeePrice(true)%26anchor%3D24%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=zh-Hans&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D',
        'https://api.nike.com.cn/cic/browse/v2?queryid=products&anonymousId=DSWX092BF0B906D9ED416BC37EAACD002AC2&country=cn&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(CN)%26filter%3Dlanguage(zh-Hans)%26filter%3DemployeePrice(true)%26anchor%3D48%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=zh-Hans&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D']

    def parse(self, response):
        lst = json.loads(response.text)['data']['products']['products']
        for _ in lst:
            yield scrapy.Request(url=f"https://www.nike.com.cn{_['url'].replace('{countryLang}', '')}", callback=self.parse_detail)


    def parse_detail(self, response):
        item = DemoItem()
        _ = json.loads(response.xpath('//script[@id = "__NEXT_DATA__"]/text()').get())['props']['pageProps']
        style_corlor = _['colorwayImages'][0]['styleColor']
        item['url'] = _['productGroups'][0]['products'][style_corlor]['productInfo']['url']
        item['title'] = _['productGroups'][0]['products'][style_corlor]['productInfo']['title']
        item['sub_title'] =  _['productGroups'][0]['products'][style_corlor]['productInfo']['subtitle']
        item['price'] = _['productGroups'][0]['products'][style_corlor]['prices']['currentPrice']
        item['color'] = _['colorwayImages'][0]['colorDescription']
        item['size'] = _['selectedProduct']['sizes'][0]['localizedLabel']
        item['sku'] = _['selectedProduct']['sizes'][0]['merchSkuId']
        item['details'] = _['productGroups'][0]['products'][style_corlor]['productInfo']['productDescription']
        item['img_urls'] = _['colorwayImages'][0]['squarishImg']

        yield item












