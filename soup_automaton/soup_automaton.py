from bs4 import BeautifulSoup, SoupStrainer
import requests

# sources = {
#     "voz": "https://voz.vn/f/may-tinh-de-ban.68/"
# }

# strainers = {
#     "voz": "structItem-title"
# }

# for source, url in sources.items():
#     page = requests.get(url)
#     if source == "voz":
#         strainers = SoupStrainer(class_=strainers[source])
#     soup = BeautifulSoup(page.text, 'lxml')
#     print(soup.prettify())
