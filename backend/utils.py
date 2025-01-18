import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

def analysis(product):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "",
            },
            {
                "role": "user",
                "content": f"""You are an expert in sustainable shopping with a vast amount of knowledge on eco-friendliness and the impact 
                of various products on the environment. You are given extracted text content from a webpage about a product. 
                Identify the product for sale and given its details, your task is to do a detailed analysis on the environmental impact of the particular 
                product on the environment. You are to do these things:
                1. Generate a short description of the product
                2. Rate the product's environment-friendliness on a scale from 0 (very harmful to the environment) to 10 (very good for the environment)
                3. Give a short summarised reason for your response in a single sentence
                4. Give a detailed reason for your response in a longer paragraph where you should mention in detail the reason for your rating 
                and educate the user about the produt's environment impact, advice them on whether they should purchase the item or not, 
                recycling options etc.
                Give your answer in the format of a python dictionary with the following keys: description, rating, summary, detail
                Do NOT include anything else in your response EXCEPT the python dictionary, no text, symbols or anything else. Do not forget to put both 
                opening and closing curly brackets.
                Extracted product details: {product}""",
            }
        ],
        model="gpt-4o-mini",
        temperature=1,
        max_tokens=1000,
        top_p=1
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content

def get_alternatives(desc):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "",
            },
            {
                "role": "user",
                "content": f"""You are a helpful assistant whose task is to search the internet for alternatives to the product whose description 
                is given to you. The alternatives should be more environmental-friendly than this product and should have less negative impact on the climate. 
                If you find links to alternatives, do mention those. Otherwise, clearly mention the product names and, if possible, brand names and purchase 
                options so the user has the maximum amount of information and resources needed to purchase the item(s). It is prefereable if you
                provide links using which users can buy the items.
                Product description: {desc}""",
            }
        ],
        model="gpt-4o-mini",
        temperature=1,
        max_tokens=500,
        top_p=1
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content