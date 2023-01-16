from selenium.webdriver.common.by import By


sources = {
    "voz": "https://voz.vn/f/may-tinh-de-ban.68/"
}

reference_elements = {
    "voz": {
        "thread": {"by": By.CLASS_NAME, "value": "structItem--thread"},
        "thread-link": {"by": By.CSS_SELECTOR, "value": "[data-tp-primary]"},
        "title": {"by": By.CLASS_NAME, "value": "structItem-title"},
        "label": {"by": By.CLASS_NAME, "value": "label"},
        "time": {"by": By.CLASS_NAME, "value": "structItem-latestDate"},
        "thread-content": {"by": By.CLASS_NAME, "value": "message-content"}
    }
}