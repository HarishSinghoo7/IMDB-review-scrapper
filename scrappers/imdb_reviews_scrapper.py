from scrappers.web_request_handler import WebRequestHandler

class IMDBReviewsScrapper:
    def __init__(self, searchStr):
        self.searchStr = searchStr
        self.__BASE_URL = "https://www.imdb.com"
        self.webHandler = WebRequestHandler()

    def getURL(self):
        # Search by title
        return f"{self.__BASE_URL}/find?s=tt&q={self.searchStr}&ref_=nv_sr_sm"

    def getReviews(self):
        try:
            getSearchHtml = self.webHandler.getHmltPageFromUrl(self.getURL())
            if not getSearchHtml:
                raise Exception(f'Unable to access the IMDB site.')
            try:
                title_results = getSearchHtml.find('table',{'class':'findList'}).find_all('tr', {'class': 'findResult'})
            except:
                title_results = []

            all_titles_reviews = []
            for i,title_result in enumerate(title_results):
                # Break after 2 iteration
                if i == 2:
                    break

                title_url = title_result.find('a')['href']
                result_title = title_result.find('td',{'class': 'result_text'}).text
                all_titles_reviews.append({'searchStr': self.searchStr.replace('+', ' '), 'result_title':result_title, 'reviews': self.processTitlePage(title_url)})
            return all_titles_reviews
        except Exception as e:
            print(str(e))

    def processTitlePage(self,title_url):
        try:
            titlePage = self.webHandler.getHmltPageFromUrl(f"{self.__BASE_URL}{title_url}")
            all_reviews_url = titlePage.find('div', {'class': 'user-comments'}).find_all('a')[-1]['href']
            return self.processAllReviews(all_reviews_url)
        except Exception as e:
            print(str(e))

    def processAllReviews(self, all_reviews_url):
        try:
            reviewsPage = self.webHandler.getHmltPageFromUrl(f"{self.__BASE_URL}{all_reviews_url}")
            reviews = []
            reviewsContainers = reviewsPage.find_all('div', {'class': 'review-container'})
            for reviewsContainer in reviewsContainers:
                reviews.append(self.getReview(reviewsContainer))
            return reviews
        except Exception as e:
            print(str(e))


    def getReview(self, reviewsContainer):
        try:
            try:
                rating = reviewsContainer.find('span', {'class':'rating-other-user-rating'}).find('span').text
            except:
                rating = 0

            item_content = reviewsContainer.find('div', {'class': 'lister-item-content'})

            try:
                title = item_content.find('a', {'class': 'title'}).text
            except:
                title = ''

            try:
                name = item_content.find('span', {'class': 'display-name-link'}).a.text
            except:
                name = ''

            try:
                review_date = item_content.find('span', {'class','review-date'}).text
            except:
                review_date = ''

            try:
                review = item_content.find('div', {'class': 'text'}).text
            except:
                review = ''

            return {'title': title, 'name': name, 'review_date': review_date, 'rating': rating, 'review': review}
        except Exception as e:
            print(str(e))
