from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from controllers.reviews_scrapper import ReviewsScrapper

app = Flask(__name__)

CORS(app)
@cross_origin()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/reviews', methods=['POST'])
def reviews():
    reviews = ReviewsScrapper(request.form['searchStr']).getReviews()
    # reviews = 'Fetching reviews'
    return render_template('reviews.html', reviews=reviews)


if __name__ == '__main__':
    app.run(port=8080, debug=True)