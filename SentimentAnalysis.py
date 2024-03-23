from sqlalchemy import create_engine
import pandas as pd

# Connection strings
cloud_db_string = 'your_cloud_database_connection_string'
on_prem_db_string = 'your_on_premises_database_connection_string'

# Create SQLAlchemy engines
cloud_engine = create_engine(cloud_db_string)
on_prem_engine = create_engine(on_prem_db_string)

# Optimized SQL queries to fetch supplier feedback
feedback_sql = """
WITH supplier_feedback AS (
    SELECT supplier_id, feedback_text
    FROM cloud_db.supplier_feedback
    UNION ALL
    SELECT supplier_id, feedback_text
    FROM on_prem_db.supplier_reviews
)
SELECT * FROM supplier_feedback;
"""

# Execute queries
feedback_data = pd.read_sql(feedback_sql, cloud_engine)  # Adjust the engine as needed

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lower case
    tokens = [word for word in tokens if word.isalpha()]  # Remove punctuation
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    return ' '.join(tokens)

# Apply preprocessing
feedback_data['processed_feedback'] = feedback_data['feedback_text'].apply(preprocess_text)

from transformers import pipeline

# Load pre-trained sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Function to perform sentiment analysis
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

# Apply sentiment analysis
feedback_data['sentiment'], feedback_data['sentiment_score'] = zip(*feedback_data['processed_feedback'].apply(analyze_sentiment))

import plotly.express as px

# Aggregate sentiment scores
supplier_sentiment = feedback_data.groupby('supplier_id')['sentiment_score'].mean().reset_index()

# Visualization
fig = px.bar(supplier_sentiment, x='supplier_id', y='sentiment_score', title='Average Sentiment Score by Supplier')
fig.update_layout(xaxis_title="Supplier ID", yaxis_title="Average Sentiment Score")
fig.show()
