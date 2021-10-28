import asyncio
import json
import urllib.request
from typing import List
import aiohttp
import bs4
from pyparsing import unicode


def get_urls_list():
    urls = []
    base_url = 'https://markets.businessinsider.com/index/components/s&p_500'
    base_page = urllib.request.urlopen(base_url)
    class_name = "finando_paging margin-top--small"
    base_soup = bs4.BeautifulSoup(base_page, 'html.parser')
    begin_of_pagination = (base_soup.find(class_=class_name).find('a'))
    first_url = base_url + begin_of_pagination['href']
    urls.append(first_url)
    while True:
        next_page = urllib.request.urlopen(urls[-1])
        next_soup = bs4.BeautifulSoup(next_page, 'html.parser')
        next_pagination = (next_soup.find(class_=class_name).find(
            'strong').parent.next_sibling.next_sibling)
        if next_pagination:
            next_url = base_url + next_pagination['href']
            urls.append(next_url)
        else:
            break
    return urls


def get_dollar_priсe() -> float:
    page = urllib.request.urlopen('https://www.cbr.ru/scripts/XML_daily.asp?')
    currency_soup = bs4.BeautifulSoup(page, 'html.parser')
    dollar_usa = currency_soup.find('valute', {'id': "R01235"})
    return float(dollar_usa.value.string.replace(',', '.'))


async def built_main_data_list(company_tag):
    data = []
    one_company_dictionary = await parse_data_from_company_page({
        'detail_url': get_one_comp(company_tag),
        'growth': float(
            company_tag.find_all('td')[-1].find_all('span')[1].string.strip(
                '% '))
    })
    data.append(one_company_dictionary)
    return data


async def get_companies_tags_from_page(url_of_page):
    async with aiohttp.ClientSession() as session:
        async with session.get(url_of_page) as resp:
            page = await resp.text()
            page_soup = bs4.BeautifulSoup(page, 'html.parser')
            companies_tags_from_one_page_list = \
                page_soup.find('tbody', class_='table__tbody').find_all('tr')
            return companies_tags_from_one_page_list


def get_one_comp(company_tag):
    company_url = 'https://markets.businessinsider.com' + company_tag.a['href']
    return company_url


def convert_navigable_string_to_int(navigable_string):
    return float(unicode(navigable_string).replace(',', ''))


def convert_str_to_float(string):
    return float(string.replace(',', ''))


async def parse_data_from_company_page(company):
    async with aiohttp.ClientSession() as session:
        async with session.get(company['detail_url']) as resp:
            company_page = await resp.text()
            company_soup = bs4.BeautifulSoup(company_page, 'html.parser')
            company_dollar_price = convert_navigable_string_to_int(
                company_soup.find(
                    'span', class_='price-section__current-value').string)
            raw_week_low = company_soup.find('div', string='52 Week Low')
            raw_week_high = company_soup.find('div', string='52 Week High')
            if raw_week_low and raw_week_high:
                week_low = convert_str_to_float(
                    list(raw_week_low.parent.strings)[0].strip())
                week_high = convert_str_to_float(
                    list(raw_week_high.parent.strings)[0].strip())
                company['potential profit'] = round(
                    (week_high - week_low) * 100 / week_low, 2)
            else:
                company['potential profit'] = 0
            pe = company_soup.find('div', string='P/E Ratio')
            if pe:
                company['P/E'] = convert_str_to_float(
                    pe.previousSibling.string.strip())
            else:
                company['P/E'] = 0
            company['name'] = company_soup.find(
                'span', class_='price-section__label').string.strip()
            company['code'] = company_soup.find(
                'span', class_='price-section__category').span.string.strip(
                ', ')
            company['price'] = round((company_dollar_price * dollar_price), 2)
            return company


async def main(pages_urls):
    companies_result_list = []
    companies_tags_list = []

    for url in pages_urls:
        companies_tags_list += await get_companies_tags_from_page(url)

    for company_tag in companies_tags_list:
        companies_result_list += await built_main_data_list(company_tag)

    return companies_result_list


def save_top_companies(companies_list, file_name, key, reverse_value):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(get_top_companies(companies_list, key, reverse_value)[0:10],
                  file,
                  sort_keys=True,
                  indent=4)


def get_top_companies(all_companies_list, key, reverse_value) -> List:
    return sorted(all_companies_list, key=lambda company: company[key],
                  reverse=reverse_value)


if __name__ == '__main__':
    dollar_price = get_dollar_priсe()
    all_pages_urls = get_urls_list()
    all_companies_list = asyncio.run(main(all_pages_urls))
    data_for_file = [
        {
            'key': 'price',
            'file_name': 'most_expencive_action_companies.json',
            'reverse_value': True
        },
        {
            'key': 'P/E',
            'file_name': 'lowes_pe_companies.json',
            'reverse_value': False
        },
        {
            'key': 'growth',
            'file_name': 'highest_growth_companies.json',
            'reverse_value': True
        },
        {
            'key': 'potential profit',
            'file_name': 'highest_potential_profit_companies.json',
            'reverse_value': True
        }
    ]
    for values_dict in data_for_file:
        save_top_companies(all_companies_list, **values_dict)
