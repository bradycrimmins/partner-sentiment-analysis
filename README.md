# Supplier Feedback Sentiment Analysis

This project demonstrates how to perform sentiment analysis on supplier feedback collected from various sources, including cloud-based and on-premises databases. The goal is to assess supplier performance by analyzing the sentiment of the feedback provided by users or automated systems.

## Overview

The code is structured to perform several key tasks:
- **Data Fetching**: Collects supplier feedback data from multiple databases using SQLAlchemy and optimized SQL queries.
- **Data Preprocessing**: Applies natural language processing (NLP) techniques to clean and prepare the feedback text for analysis.
- **Sentiment Analysis**: Uses a pre-trained model from the `transformers` library to analyze the sentiment of each piece of feedback.
- **Visualization**: Aggregates sentiment scores by supplier and visualizes the results using Plotly for easy interpretation.

## Requirements

To run this code, you will need:
- Python 3.x
- SQLAlchemy
- Pandas
- NLTK
- Transformers library (Hugging Face)
- Plotly

Ensure you have the necessary libraries installed by running:
```
pip install sqlalchemy pandas nltk transformers plotly
```

Additionally, you'll need to have access to the cloud and on-premises databases where the feedback data is stored. Make sure to replace the placeholder connection strings with your actual database connection strings.

## Steps

1. **Database Connection**: Establish connections to both cloud and on-premises databases using SQLAlchemy engines.
   
2. **Data Fetching**: Execute SQL queries to retrieve feedback data, combining information from both data sources.

3. **Text Preprocessing**: Clean the feedback text by tokenizing, converting to lowercase, removing punctuation and stopwords to prepare the data for sentiment analysis.

4. **Sentiment Analysis**: Analyze the preprocessed feedback text using the sentiment analysis pipeline from the `transformers` library to classify sentiments as positive, negative, or neutral, along with a confidence score.

5. **Results Aggregation and Visualization**: Aggregate the average sentiment scores by supplier and visualize the results using Plotly to identify suppliers with the highest and lowest sentiment scores.

## Usage

Replace the database connection strings with your actual credentials. Execute the script to fetch the data, preprocess the text, perform sentiment analysis, and visualize the results.

This script is a powerful tool for understanding supplier performance from a qualitative perspective, allowing businesses to make informed decisions based on the sentiment of feedback received.

## Customization

Consider extending the script to include:
- More sophisticated text preprocessing steps based on specific characteristics of your feedback data.
- Fine-tuning the sentiment analysis model with domain-specific data to improve accuracy.
- Incorporating additional data sources or feedback channels for a more comprehensive analysis.

## License

This project is open-source and free for personal or commercial use.
