from textblob import TextBlob

NEGATIVE_KEYWORDS = [
    "need improvement", "bad", "slow", "problem", "poor", "worst"
]

def analyze_sentiment(text):
    text_lower = text.lower()

    for word in NEGATIVE_KEYWORDS:
        if word in text_lower:
            return "Negative"

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    else:
        return "Neutral"

def generate_reply(sentiment):
    if sentiment == "Positive":
        return "Thank you for your positive feedback. We are glad you had a good experience."
    elif sentiment == "Negative":
        return "Thank you for sharing your concerns. We will work on improving the mentioned areas."
    else:
        return "Thank you for your valuable feedback. Your suggestions help us improve."
