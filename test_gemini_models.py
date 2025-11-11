"""
Test script to list available Gemini models
This will help us see what model names actually work with your API key
"""
import google.generativeai as genai

# You'll need to paste your API key here
API_KEY = input("Enter your Gemini API key: ")

genai.configure(api_key=API_KEY)

print("\n=== Available Gemini Models ===\n")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Model: {model.name}")
        print(f"  Display Name: {model.display_name}")
        print(f"  Description: {model.description}")
        print(f"  Supported methods: {model.supported_generation_methods}")
        print()
