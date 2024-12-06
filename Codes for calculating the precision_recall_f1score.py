import pandas as pd

# Load the Excel file (replace 'your_file.xlsx' with your actual file path)
df = pd.read_excel('1.xlsx')

# Specify columns for each LLM's predictions and the actual sentiment
llm_columns = ['llama3.2', 'gemma2', 'phi3']
actual_column = 'Sentiment'

# Convert all text to lowercase for uniformity
df[llm_columns + [actual_column]] = df[llm_columns + [actual_column]].apply(lambda x: x.str.lower())

# List of sentiments
sentiments = ['positive', 'negative', 'neutral']


# Define a function to calculate precision, recall, and F1-score manually for a specific sentiment
def calculate_metrics_for_sentiment(predictions, actuals, target_sentiment):
    # Initialize counters for TP, FP, and FN
    true_positive = false_positive = false_negative = 0

    # Calculate TP, FP, and FN
    for pred, actual in zip(predictions, actuals):
        if pred == target_sentiment:
            if actual == target_sentiment:
                true_positive += 1  # Correctly predicted as target sentiment
            else:
                false_positive += 1  # Incorrectly predicted as target sentiment
        elif actual == target_sentiment:
            false_negative += 1  # Failed to predict the target sentiment when it was actual

    # Calculate precision, recall, and F1-score
    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
    f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return precision, recall, f1_score


# Initialize a dictionary to store results for each LLM and each sentiment
results = {}

# Calculate metrics for each LLM and each sentiment
for llm in llm_columns:
    results[llm] = {}
    for sentiment in sentiments:
        precision, recall, f1_score = calculate_metrics_for_sentiment(df[llm], df[actual_column], sentiment)
        results[llm][sentiment] = {
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1_score
        }

    # Calculate weighted average precision and recall for the LLM
    total_instances = len(df)

    # Count the number of instances for each sentiment in the actual column
    sentiment_counts = df[actual_column].value_counts()

    weighted_precision = 0
    weighted_recall = 0
    for sentiment in sentiments:
        sentiment_count = sentiment_counts.get(sentiment, 0)
        sentiment_precision = results[llm].get(sentiment, {}).get('Precision', 0)
        sentiment_recall = results[llm].get(sentiment, {}).get('Recall', 0)

        # Calculate weighted precision and recall
        weighted_precision += sentiment_precision * (sentiment_count / total_instances)
        weighted_recall += sentiment_recall * (sentiment_count / total_instances)

    # Calculate F1-score based on weighted precision and recall
    if (weighted_precision + weighted_recall) > 0:
        weighted_f1_score = 2 * weighted_precision * weighted_recall / (weighted_precision + weighted_recall)
    else:
        weighted_f1_score = 0

    results[llm]['Weighted Precision'] = weighted_precision
    results[llm]['Weighted Recall'] = weighted_recall
    results[llm]['Weighted F1-Score'] = weighted_f1_score

# Display the results with four significant digits
for llm, metrics in results.items():
    print(f"Results for {llm}:")
    for sentiment, scores in metrics.items():
        if sentiment not in ['Weighted Precision', 'Weighted Recall', 'Weighted F1-Score']:
            print(f"  Sentiment: {sentiment.capitalize()}")
            print(f"    Precision: {scores['Precision']:.4f}")
            print(f"    Recall: {scores['Recall']:.4f}")
            print(f"    F1-Score: {scores['F1-Score']:.4f}")
    print(f"  Weighted Precision: {metrics['Weighted Precision']:.4f}")
    print(f"  Weighted Recall: {metrics['Weighted Recall']:.4f}")
    print(f"  Weighted F1-Score: {metrics['Weighted F1-Score']:.4f}")
    print()
