
from dotenv import load_dotenv
from google import genai
from main import main as instruction
from main import plans as plans
from main import end_statement as ender
from main import combiner


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


def AI_handler_with_input(get_content="Analyze the following content."):
    """Reads pasted text from the terminal and sends it to Gemini."""
    main_content = get_content

    pasted_text = combiner()

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=main_content + "\n\n" + pasted_text
    )

    return response.text


# Do not uncomment the lines below, they are for testing purposes only.
print(AI_handler_with_input())
