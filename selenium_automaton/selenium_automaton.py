from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
import retry
import time

from sources import reference_elements, sources


service = FirefoxService(executable_path=GeckoDriverManager().install())

def __init_driver():
    ff_option = webdriver.FirefoxOptions()
    ff_option.headless = True
    return webdriver.Firefox(service=service, options=ff_option)

def go_to_web_and_fetch_title(url: str):
    with __init_driver() as driver:
        driver.get(url)
        title = driver.title
    return title

def get_items_based_on_prompt(source: str, prompt: str, tag: str | None = None, dig_deep=False) -> list:
    source = "voz"  # Testing
    source_ref = reference_elements[source]
    result = []
    pages = 1
    with __init_driver() as driver:
        while pages <= 5:
            if (pages == 1):
                driver.get(sources[source])
                pages += 1
            else:
                driver.get("".join([sources[source], f"page-{pages}"]))
                print("".join([sources[source], f"page-{pages}"]))
                pages += 1
            thread_elements = driver.find_elements(**source_ref['thread'])
            print(thread_elements.__len__())
            for topic in thread_elements:
                if topic.find_elements(**source_ref['label']).__len__() == 0:
                    continue
                if tag != topic.find_element(**source_ref['label']).text:
                    pass
                else:
                    if prompt in topic.find_element(**source_ref['title']).text:
                        # print(topic.find_element(**source_ref['title']).text)
                        result.append(
                            topic.find_element(**source_ref['thread-link']).get_attribute("href")
                        )
                    elif dig_deep:
                        pass
    return result
