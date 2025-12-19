from flask import Flask, render_template, redirect
from selenium_scraper import scrape_reviews
from bot import analyze_sentiment, generate_reply

app = Flask(__name__)

reviews_data = []
REVIEW_URL = "https://www.trustpilot.com/review/www.flipkart.com"

@app.route("/")
def dashboard():
    return render_template("dashboard.html", reviews=reviews_data)

@app.route("/scrape", methods=["POST"])
def scrape():
    reviews_data.clear()

    reviews = scrape_reviews(REVIEW_URL)

    for idx, review in enumerate(reviews, start=1):
        sentiment = analyze_sentiment(review)
        reply = generate_reply(sentiment)

        reviews_data.append({
            "id": idx,
            "review": review,
            "sentiment": sentiment,
            "reply": reply
        })

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
