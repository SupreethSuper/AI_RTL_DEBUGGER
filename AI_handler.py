

import os
from dotenv import load_dotenv
from google import genai


# Load your .env file
load_dotenv() 

# The Client will automatically look for an environment variable 
# named 'GOOGLE_API_KEY' since we loaded it above.

def AI_handler(get_content):
    client = genai.Client() 

    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=get_content
    )

    return response.text