import requests
from bs4 import BeautifulSoup

url_list = ["planqc.eu", "kipu-quantum.com"]

def get_site_text_content(url: str) -> str:
    """Given a url, get only the text content of this site"
    @param url: str. The root url we want to parse for text.
    @return str. Text content of the url
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def get_sitemap_urls(root_url: str) -> list[str]:
    """Tries to get all urls from the sitemap.
    If the sitemap doesn't exist, just return the original URL.
    @param url: The root url from which we want to get all subpages
    @return list of subpages
    """

    sitemap_url = root_url + '/sitemap.xml'
    response = requests.get(sitemap_url)

    # always have original url in the set
    # use set to deduplicate

    sitemap_urls = []

    # better solution: go recursive. Do that later :)
    # extract urls until there is no xml anymore
    if response:
        soup = BeautifulSoup(response.text, features='xml')

        sitemap_urls = [loc.text for loc in soup.find_all('loc')]

    return root_url + sitemap_urls

def get_text_from_all_subpages(url):
    pass

def get_text_from_all_subpages(root_url):

    urls = get_sitemap_urls(root_url)

    for url in urls:
        text_content = get_site_text_content(url)
        filename = './data/text_data/' + url.replace('/', '_') + '.txt'
        with open(filename, 'w') as file:
            file.write(text_content)


def main():
    pass


if __name__ == '__main__':
    main()