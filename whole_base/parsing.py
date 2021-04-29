import requests
from bs4 import BeautifulSoup

data_list = []


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1'
    }
    response = requests.get(url, headers=headers)
    return response.text


def parsing(url):
    global titles, images, prices
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    main = soup.find('div', {'id': 'listing-container'}).find('ul', class_='GridInner_list___8u79').find_all('li', class_='ListingProductCardList_productCardListingWrapper__3-o9i')

            titles[i] = product.find('div', class_='ListingProductCardList_productCardListingDescription__q4iOE').find('a', class_='ListingProductCardList_productCardListingLink__1JIMi').text
            images[i] = product.find('img', class_='ListingProductCardImage_listingProductCardImage__2fGmx').get('src')
            prices[i] = product.find('span', class_='PriceBlock_buyBoxPrice__3QGyj PriceBlock_buyBoxPriceStyled__29J_G').text.replace('\xa0', ' ')
        name_title = ''
    for i in range(1, len(titles)+1):
        name_title += f'{i}: {titles[i]}\n'
    return name_title, images, prices
