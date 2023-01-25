from bs4 import BeautifulSoup
from operator import itemgetter  # для сортировки по индексу
import pandas as pd  # используем для записи в csv
import json
import time
import asyncio
import aiohttp

cars_for_csv = []
cars_for_json = []
header = ["BMW_X7_link", "BMW_X7_price_BYN", "BMW_X7_price_USD", "BMW_X7_engine"]
start_time = time.time()


async def bmw_x7_on_the_page(page):
    async with aiohttp.ClientSession() as session:
        url = f"https://cars.av.by/filter?brands[0][brand]=8&brands[0][model]=5965&page={page}"
        async with session.get(url=url) as response:
            response_text = await response.text()
            soup = BeautifulSoup(response_text, 'lxml')
            bmw_x7_all = soup.find_all('div', class_="listing-item")

            for bmw_x7 in bmw_x7_all:
                bmw_x7_link = "https://cars.av.by" + bmw_x7.find('a', class_='listing-item__link').get('href')
                bmw_x7_price_byn = bmw_x7.find('div', class_='listing-item__price').text.replace("\xa0", " ") \
                    .replace("\u2009", "").replace(" р.", "")
                bmw_x7_price_usd = bmw_x7.find('div', class_='listing-item__priceusd').text.replace("≈", "") \
                    .replace("\xa0", "").replace("\u2009", "").replace("$", "")
                bmw_x7_engine = bmw_x7.find('div', class_='listing-item__params').text.replace("\xa0", " ") \
                    .replace("\u2009", "")

                cars_for_csv.append([bmw_x7_link, int(bmw_x7_price_byn), int(bmw_x7_price_usd), bmw_x7_engine])
                cars_for_json.append({header[0]: bmw_x7_link, header[1]: int(bmw_x7_price_byn),
                                      header[2]: int(bmw_x7_price_usd), header[3]: bmw_x7_engine})


async def pages():
    tasks = []

    for page in range(1, 3):
        task = asyncio.create_task(bmw_x7_on_the_page(page))
        tasks.append(task)

    await asyncio.gather(*tasks)


def main():
    asyncio.run(pages())

    cars_csv_sorted = sorted(cars_for_csv, key=itemgetter(2))  # сортируем по 2 индексу (USD)
    cars_json_sorted = sorted(cars_for_json, key=itemgetter('BMW_X7_price_USD'))  # сортируем по ключу "BMW_X7_price_US"
    print(cars_csv_sorted)
    print(cars_json_sorted)

    cars_bmw_x7 = pd.DataFrame(cars_csv_sorted, columns=header)
    cars_bmw_x7.to_csv('cars_bmw_x7.csv', sep=':', encoding='utf-8-sig')

    with open('cars_bmw_x7.json', 'w', encoding='UTF-8') as file:
        json.dump(cars_json_sorted, file, ensure_ascii=False)

    finish_time = time.time() - start_time
    print(f"Затраченное на работу скрипта время: {finish_time}")


if __name__ == "__main__":
    main()
