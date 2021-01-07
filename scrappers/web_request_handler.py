from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

class WebRequestHandler:
    def getHmltPageFromUrl(self, searchUrl):
        """
         Requesting search url
         :param str search url
         :return HTML result of search page
        """
        print(searchUrl)
        try:
            uClient = urlopen(searchUrl)  # Requesting webpage from internet
            htmlPage = uClient.read()
            uClient.close()
            htmlPage = bs(htmlPage, 'html.parser')
            return htmlPage
        except Exception as e:
            raise e