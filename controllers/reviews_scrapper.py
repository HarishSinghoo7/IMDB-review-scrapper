from scrappers.imdb_reviews_scrapper import IMDBReviewsScrapper
from models.mongodb import MongoDB

class ReviewsScrapper:
    def __init__(self, searchStr):
        self.searchStr = searchStr.replace(' ','+')
        self.dbHandler, self.scrapper = self.__configure()

    def __configure(self):
        try:
            dbHandler = MongoDB()
            scrapper = IMDBReviewsScrapper(self.searchStr)
            return dbHandler, scrapper
        except Exception as e:
            print(str(e))

    def getReviews(self):
        try:
            results = self.dbHandler.fetchData(self.searchStr)
            if len(results):
                return results
            else:
                reviews = self.scrapper.getReviews()
                if len(reviews) > 0:
                    self.dbHandler.saveMany(self.searchStr,reviews)
                return reviews
        except Exception as e:
            print(str(e))
