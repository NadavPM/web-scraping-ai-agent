"""
Test how langchain-google-genai handles model names
This will show us what's actually being sent to the API
"""
from langchain_google_genai import ChatGoogleGenerativeAI

API_KEY = input("Enter your Gemini API key: ")

# Test different model name formats
model_names = [
    "gemini-pro",
    "models/gemini-pro",
    "gemini-1.5-pro",
    "models/gemini-1.5-pro",
    "gemini-1.5-flash",
    "models/gemini-1.5-flash",
]

print("\n=== Testing Model Names ===\n")
for model_name in model_names:
    print(f"Testing: {model_name}")
    try:
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=API_KEY,
            temperature=0
        )
        # Try a simple prompt
        response = llm.invoke("Say hello")
        print(f"  ✅ SUCCESS: {model_name}")
        print(f"  Response: {response.content[:50]}...")
    except Exception as e:
        print(f"  ❌ FAILED: {str(e)[:100]}")
    print()
