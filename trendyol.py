import requests
from urllib.parse import urlparse, parse_qs
import re


def main():
    url = input('Enter the product id or url: ').strip()

    if re.match(r'https://www.trendyol.com/.*', url):
        product_id = re.search(r'p-(\d+)', url).group(1)
    else:
        product_id = url

    api = 'https://public.trendyol.com/discovery-web-productgw-service/api/productDetail/{}'.format(product_id)
    response = requests.get(api)
    data = response.json()
    merchants = []
    if data['result'] is not None:
        other_merchants_url = data['result']['otherMerchants']
    for i in range(len(other_merchants_url)):
        merchant = parse_qs(urlparse(other_merchants_url[i]['url']).query)['merchantId'][0]
        merchant_url = 'https://www.trendyol.com/magaza/trendyol-m-' + merchant + '?sst=0'
        print(merchant_url)
        merchants.append(merchant_url)
    with open('merchants.txt', 'a') as f:
        f.write('\n' + url + ' merchants:\n')
        for merchant in merchants:
            f.write('\t' + merchant + '\n')


if __name__ == '__main__':
    main()
