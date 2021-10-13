import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
from paths import webdriver_path, folder_for_pdf

RECEIVER_ADDRESS = 'kot.siniy@mail.ru'
SUBJECT = 'A xlsx file'
FILE_NAME = 'result.xlsx'
QUERY = 'shell analysis'
N_PAGE = 1
QUERY_LINK = f'https://www.semanticscholar.org/search?q={QUERY}&sort=relevance&page='
TIMEOUT = 5


def create_webdriver():
    chrome_options = Options()

    prefs = {
        'download.default_directory': folder_for_pdf,
        'download.prompt_for_download': False,
        'download.extensions_to_open': "applications/pdf"
    }
    chrome_options.add_experimental_option('prefs', prefs)

    return webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)
