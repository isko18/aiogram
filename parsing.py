# from bs4 import BeautifulSoup
# import requests

# count_news = 0
# with open('news.txt', 'rb', encoding='utf=8') as file:
#     for page in range(1, 11):
#         url = f'https://24.kg/page_{page}'
#         response = requests.get(url=url)
#         print(response)
#         soup = BeautifulSoup(response.text, 'lxml')
#         all_news = soup.find_all('div', class_='title')
#         # print(all_news)

#         for news in all_news:
#             count_news += 1
#             file.write(f'{count_news}. {news.text}\n')
#             # print(count_news, news.text)

import requests
from bs4 import BeautifulSoup

def get_laptops():
    url = 'https://www.sulpak.kg/f/noutbuki'
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')

    laptops = []
    product_containers = soup.select('.product__item-inner')
    if not product_containers:
        print("No products found. Check the selectors.")
        return laptops

    for item in product_containers:
        title_element = item.select_one('.product__item-name a')
        price_element = item.select_one('.product__item-price')
        if title_element and price_element:
            title = title_element.get_text(strip=True)
            price = price_element.get_text(strip=True).replace('сом', '').strip()
            laptops.append({
                'title': title,
                'price': price
            })

    return laptops

# if __name__ == '__main__':
#     laptops = get_laptops()
#     if laptops:
#         for laptop in laptops:
#             print(f"{laptop['title']}\nЦена: {laptop['price']} сом\n")
#     else:
#         print("No laptops found.")


laptop = get_laptops()
if not laptop:
    await message.reply("не получилось")
    return
for laptop in laptops:
    await message.reply(f'{laptop['title']}\nцена {laptop['price'] com}')