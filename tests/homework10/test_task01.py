import os

import pytest

from homework10.task01 import (get_dollar_priсe, get_urls_list,
                               save_top_companies)


def test_get_dollar_prise():
    assert isinstance(get_dollar_priсe(), float)


def test_get_urls_list_is_list():
    assert isinstance(get_urls_list(), list)


def test_get_urls_list_len():
    assert len(get_urls_list()) == 11


@pytest.fixture
def delete_file():
    yield None
    os.remove('most_expencive_action_companies.json')


def test_save_top_companies_price(delete_file):
    companies_list = [
        {
            "P/E": 17.87,
            "code": "NVR",
            "detail_url":
                "https://markets.businessinsider.com/stocks/nvr-stock",
            "growth": 12.4,
            "name": "NVR Inc.",
            "potential profit": 37.85,
            "price": 356219.97
        },
        {
            "P/E": 79.54,
            "code": "AMZN",
            "detail_url":
                "https://markets.businessinsider.com/stocks/amzn-stock",
            "growth": -5.7,
            "name": "Amazon",
            "potential profit": 30.96,
            "price": 243028.98
        },
        {
            "P/E": 30.01,
            "code": "GOOG",
            "detail_url":
                "https://markets.businessinsider.com/stocks/goog-stock",
            "growth": 73.97,
            "name": "Alphabet C (ex Google)",
            "potential profit": 93.87,
            "price": 202162.36
        }]
    file_name = 'most_expencive_action_companies.json'
    key = 'price'
    reverse_value = True
    print(os.getcwd())
    save_top_companies(companies_list, file_name, key, reverse_value)
    assert os.path.exists(file_name)
