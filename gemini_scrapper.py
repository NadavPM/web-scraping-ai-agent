# Import the required libraries
import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph

# Set up the Streamlit app
st.title("Web Scraping AI Agent 🕵️‍♂️")
st.caption("This app allows you to scrape a website using Google Gemini API")

# Get Google API key from user
google_api_key = st.text_input("Google API Key (Gemini)", type="password")

if google_api_key:
    model = st.radio(
        "Select the Gemini model",
        ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-flash-latest", "gemini-pro-latest"],
        index=0,  # Default to gemini-2.5-flash (fast and stable)
        help="Flash is faster and cheaper, Pro is more capable. 'Latest' models auto-update."
    )

    graph_config = {
        "llm": {
            "api_key": google_api_key,
            "model": f"google_genai/{model}",
            "temperature": 0,
        },
        "verbose": True,
        "headless": True,
    }

    # Get the URL of the website to scrape
    url = st.text_input("Enter the URL of the website you want to scrape")

    # Get the user prompt
    user_prompt = st.text_input("What you want the AI agent to scrape from the website?")

    # Scrape the website
    if st.button("Scrape"):
        if not url:
            st.error("Please enter a URL")
        elif not user_prompt:
            st.error("Please enter what you want to scrape")
        else:
            with st.spinner("Scraping website..."):
                try:
                    # Create a SmartScraperGraph object
                    smart_scraper_graph = SmartScraperGraph(
                        prompt=user_prompt,
                        source=url,
                        config=graph_config
                    )
                    result = smart_scraper_graph.run()
                    st.success("Scraping completed!")
                    st.write(result)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
else:
    st.info("👆 Please enter your Google API key to get started")
    st.markdown("""
    ### How to get your Google API key:
    1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
    2. Click "Create API Key"
    3. Copy and paste the key above

    ### Note:
    - Gemini Flash is faster and cheaper for most tasks
    - Gemini Pro is more capable for complex scraping
    """)
