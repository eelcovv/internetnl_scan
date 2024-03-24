# -*- coding: utf-8 -*-

import pytest
from internetnl_scan.utils import (
    get_clean_url,
    convert_url_list,
    remove_sub_domains,
    remove_sub_domain,
    get_urls_from_domain_file,
)

__author__ = "Eelco van Vliet"
__copyright__ = "Eelco van Vliet"
__license__ = "mit"


def test_clean_url():
    clean_url, suffix = get_clean_url(url="www.example.org")
    assert clean_url == "www.example.org"
    assert suffix == "org"


def test_clean_url_with_cache():
    clean_url, suffix = get_clean_url(url="www.example.org", cache_dir="cache")
    assert clean_url == "www.example.org"
    assert suffix == "org"


def test_clean_url_list():
    urls = ["www.example.org", "www.google.nl"]

    clean_urls = convert_url_list(urls)
    assert clean_urls == urls


def test_remove_subdomain():
    assert remove_sub_domain("www.example.org") == "example.org"
    assert remove_sub_domain("https://www.google.nl") == "google.nl"


def test_remove_subdomain_from_list():

    urls = ["www.example.org", "https://www.google.nl"]
    expected_urls = ["example.org", "google.nl"]

    clean_urls = remove_sub_domains(urls)

    assert clean_urls == expected_urls


def test_get_urls_from_domain_file():

    expected_urls = [
        "https://www.google.nl",
        "https://www.example.org",
        "www.example.org",
    ]

    example_file = "url_file_no_header_one_column.txt"
    urls = get_urls_from_domain_file(example_file)
    assert urls == expected_urls

    example_file = "url_file_header_one_column.txt"
    urls = get_urls_from_domain_file(example_file, url_column_key="domain_names")
    assert urls == expected_urls

    example_file = "url_file_header_two_column.txt"
    urls = get_urls_from_domain_file(example_file, url_column_key="domain_names")
    assert urls == expected_urls

    example_file = "url_file_no_header_two_column.txt"
    urls = get_urls_from_domain_file(example_file, column_number=1)
    assert urls == expected_urls
