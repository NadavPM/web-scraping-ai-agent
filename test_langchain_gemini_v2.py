"""
Test CURRENT Gemini model names with langchain
Based on the models available in your API
"""
from langchain_google_genai import ChatGoogleGenerativeAI

API_KEY = input("Enter your Gemini API key: ")

# Test the ACTUAL current model names
model_names = [
    "gemini-2.5-flash",
    "models/gemini-2.5-flash",
    "gemini-2.5-pro",
    "models/gemini-2.5-pro",
    "gemini-flash-latest",
    "models/gemini-flash-latest",
    "gemini-pro-latest",
    "models/gemini-pro-latest",
    "gemini-2.0-flash",
    "models/gemini-2.0-flash",
]

print("\n=== Testing CURRENT Model Names ===\n")
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
        error_msg = str(e)[:150]
        print(f"  ❌ FAILED: {error_msg}")
    print()
