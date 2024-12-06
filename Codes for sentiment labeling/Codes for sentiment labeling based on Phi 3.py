import requests
import json
import csv

input_csv = "all SMD.csv"
output_csv = "all SMD_sentiment_llama3.2"

# API
url = "http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json"
}

# Define the prompt
def query_llm(context):
    prompt = (f"You are an expert in sentiment labeling. Your task is to determine whether the sentiment of the following phrase is positive, neutral, or negative.\n\n"
              f"Output only one word without any additional symbols or characters.\n"
              f"Example:\n"
              f"Q: I have yet to find AI impressive\n"
              f"A: Negative\n\n"
              f"Begin!\n"
              f"Phase: {context}"
    )

    # Print the prompt and response
    print(f"Prompt: {prompt}")

    data = {
            "model": "Phi3",
        "prompt": prompt,
        "stream": False
    }

    # 发起POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 检查响应状态
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]

        # 打印API的回答
        print(f"Response: {actual_response}\n")

        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None

# 读取CSV文件并处理
with open(input_csv, mode='r', encoding='utf-8') as infile, open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)

    # Ensure the input CSV has been read correctly
    print("Input CSV columns:", reader.fieldnames)

    # 在原有字段上添加新列 'Sentiment'
    fieldnames = reader.fieldnames + ['Sentiment']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()  # 写入表头（包括原列和新列）

    # 对每一行进行处理
    for row in reader:
        context = row['text']  # 假设 'text' 是评论所在列的名称
        sentiment = query_llm(context)  # 调用函数获取LLM响应

        # Add debug print to show the current row and sentiment
        print(f"Current row: {row}, Sentiment: {sentiment}")

        if sentiment:
            row['Sentiment'] = sentiment  # 将LLM的响应结果写入新的 'Sentiment' 列
        else:
            row['Sentiment'] = "Error"  # 如果请求失败，写入 'Error'

        # Print the row being written to the output file for debugging
        print(f"Writing row to output: {row}")
        writer.writerow(row)  # 将修改后的行写入输出文件

# Close the file properly
outfile.flush()
outfile.close()
print("All rows have been processed and written to the output file.")
