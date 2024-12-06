import requests
import json
import csv
import time

# File path definitions
input_csv = "negative_R01.csv"
output_csv = "negative_R01_OP.csv"  # Output file for positive sentiment

# API address and headers
url = "http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json"
}

# Define function for topic classification based on positive sentiment
def classify_positive_topic(context):
    # Correctly insert context using an f-string
    topic_prompt = (
        f"You are an expert in topic labeling. Your task is to classify the following text into one of the topics below by providing only the category code (A-NT1, A-NT2, T-NT3, T-NT4, S-NT5, S-NT6, S-NT7, or O-NT8), you don’t need to be strict about every word, just slight relevance is fine.\n\n"
        f"A-NT1: AI-caused energy demand increase - More energy in data centers is consumed for AI development.\n"
        f"A-NT2: Concerns regarding renewable energy - Worries about the safety, cost, environmental impact, and effectiveness of some renewable energy sources like nuclear and solar energy.\n"
        f"T-NT3: Insufficient openness of technologies - Insufficient information disclosure of data center energy efficiency strategies and performance.\n"
        f"T-NT4: Unsatisfactory site selection - Negative concerns toward current site selection.\n"
        f"S-NT5: Global warming - Energy consumption of data centers contributes to global warming.\n"
        f"S-NT6: Unequal AI technology accessibility - Some people may benefit more from AI technologies (e.g., LLM) while others benefit less.\n"
        f"S-NT7: Rising energy prices - The prices of some energy increase, such as oil, gas, electricity, and water.\n "
        f"U-NT8: Other complains \n\n"
        f"Output only the category code (A-NT1, A-NT2, T-NT3, T-NT4, S-NT5, S-NT6, S-NT7, or U-NT8) without any additional symbols or characters.\n\n"
        f" Example:\n\n"
        f"Q: No no not really. The ballooning data center industry is due to the absolutely worthless AI boom.\n"
        f"A: A-NT1\n"
        f"Now, classification begins！\n"
        f"Text: {context}\n"
    )

    # Print the topic prompt for each inquiry
    print(f"Topic Prompt: {topic_prompt}")

    data = {
        "model": "Gemma2",
        "prompt": topic_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"].strip()  # Strip any whitespace from the response
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None

# Start timing
start_time = time.time()

# Read CSV file and process
with open(input_csv, mode='r', encoding='utf-8') as infile, open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['text', 'Topic']  # Only include 'text' and 'Topic'
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()  # Write header
    outfile.flush()  # Ensure the header is written to disk immediately

    # Process each row for positive sentiment
    for row in reader:
        context = row.get('text', '')  # Get text from the current row, default to empty string if missing
        if context:  # Only proceed if context is not empty
            topic = classify_positive_topic(context)  # Get topic classification response
            if topic:
                writer.writerow({'text': context, 'Topic': topic})  # Write only 'text' and 'Topic'
                outfile.flush()  # Flush output to ensure each row is written to the file immediately

# End timing
end_time = time.time()

# Calculate and print the total run time
total_time = end_time - start_time
print(f"Total run time: {total_time:.2f} seconds")
