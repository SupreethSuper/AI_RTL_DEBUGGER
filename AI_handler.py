

import os
from dotenv import load_dotenv
from google import genai

# Load your .env file
load_dotenv() 

# The Client will automatically look for an environment variable 
# named 'GOOGLE_API_KEY' since we loaded it above.
# client = genai.Client() 

response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Hello! Are you working now?"
)

print(response.text)