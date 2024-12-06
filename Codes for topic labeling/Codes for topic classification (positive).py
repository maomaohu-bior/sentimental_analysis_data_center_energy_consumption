import requests
import json
import csv
import time

# File path definitions
input_csv = "positive_R01.csv"
output_csv = "positive_R01_OP.csv"  # Output file for positive sentiment

# API address and headers
url = "http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json"
}

# Define function for topic classification based on positive sentiment
def classify_positive_topic(context):
    # Correctly insert context using an f-string
    topic_prompt = (
        f"You are an expert in topic labeling. Your task is to classify the following text into one of the topics below by providing only the category code (A-PT1, A-PT2, A-PT3, D-PT4, D-PT5, D-PT6, D-PT7, C-PT8, C-PT9, or C-PT10), you don’t need to be strict about every word, just slight relevance is fine. YOU CAN ONLY MAKE A DECISION AFTER FULLY UNDERSTAND EACH TOPIC’ MEANING:\n\n"
        f"A-PT1: AI-assisted hardware optimization - refer to The AI technologies like optimization algorithms, are being applied to enhance hardware efficiency, including but not limited to cooling systems, air-condition systems, et al.\n"
        f"A-PT2: AI-driven renewable energy utilization - refer to The emergence of AI has compelled the exploration of renewable energy sources, including but not limited to nuclear energy, solar energy, hydroenergy, and geothermal energy, et al.\n"
        f"A-PT3: AI-promoted economic growth - refer to The overall economic growth can lead to higher incomes, job creation improved living standards, or more innovations et al., making the increased energy consumption as a necessary trade-off for progress.\n"
        f"T-PT4: Efficient device management in data centers - refer to	Optimizing the management of hardware like monitoring device usage, automating control to reduce energy consumption, and preventing unnecessary wear on equipment, et al.\n"
        f"T-PT5: Satisfactory site selection - refer to praise for current data center site selection. \n"
        f"T-PT6: Sufficient openness of technologies - refer to	Praises to current level and methods of information disclosure.\n"
        f"T-PT7: Demand-sides response in data center - refer to Adjusting the energy use of data centers based on electricity grid demands and helping stabilize the grid and save on energy costs.\n"
        f"S-PT8: Government’s investments - refer to Government investments in energy-saving and emission-reduction.\n"
        f"S-PT9: Declining energy prices - refer to The prices of some energy sources have declined in recent days.\n"
        f"U-PT10: Other praises.\n\n"
        f"Output only the category code (A-PT1, A-PT2, A-PT3, T-PT4, T-PT5, T-PT6, T-PT7, S-PT8, S-PT9, or U-PT10) without any additional symbols or characters.\n\n"
        f" Example:\n\n"
        f"Q: Texas has led the US in new renewable capacity since the passage of the clean--boosting Inflation Reduction Act two years ago! On its own, it has made up 37% of new US wind capacity, 29% of new US battery capacity, and 23% of new US solar capacity.\n"
        f"A: S-PT8\n"
        f"Now, classification begins！\n"
        f"Text: {context}\n"
    )

    # Print the topic prompt for each inquiry
    print(f"Topic Prompt: {topic_prompt}")

    data = {
        "model": "llama3.1",
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
