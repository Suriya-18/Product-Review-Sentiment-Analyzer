import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

# Download required data
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Sample product reviews
reviews = [
    "This product is amazing! I love it.",
    "Worst experience ever. Never buying again!",
    "It's okay, but could be better.",
    "I am so happy with this purchase!",
    "Not worth the money. Very disappointed."
]

# Function to analyze sentiment
def analyze_sentiment(review):
    score = sia.polarity_scores(review)
    if score['compound'] > 0.05:
        return "Positive"
    elif score['compound'] < -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
results = {"Review": reviews, "Sentiment": [analyze_sentiment(r) for r in reviews]}

# Convert to DataFrame
df = pd.DataFrame(results)
print(df)
