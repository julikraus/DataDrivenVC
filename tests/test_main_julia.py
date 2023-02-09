from src.main_julia import get_sitemap_urls, get_site_text_content
import pytest
url_list = ["planqc.eu", "kipu-quantum.com"]


def test_get_sitemap_urls_planqc():
    """There should be three sites in the sitemap"""
    urls = get_sitemap_urls("https://planqc.eu")
    assert len(urls) == 3

    assert urls[0] == 'https://planqc.eu/'
    assert urls[1] == 'https://planqc.eu/imprint/'
    assert urls[2] == 'https://planqc.eu/privacy/'

def test_get_sitemap_urls_kipu_quantum():
    """There should be three sites in the sitemap. Problem here: sitemap is
    recursively another xml."""
    #TODO: Possible strategies to deal with recursive sitemaps
    # Just parse root page: add root page always to urls and then dedupe
    urls = get_sitemap_urls("https://kipu-quantum.com")
    assert len(urls) > 0
    assert len(urls) == 4


def test_get_site_text_content():
    """The function should output the text content of the given url"""
    text_content = get_site_text_content("https://planqc.eu")
    assert text_content is not None
    assert type(text_content) == str
    assert len(text_content) > 0

