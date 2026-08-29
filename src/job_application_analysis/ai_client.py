from dotenv import load_dotenv
from mistralai.client import Mistral
import os

# uv run python -m job_application_analysis.ai_client

load_dotenv()

api_key = os.getenv("MISTRALAI_API_KEY")

mistral_client = Mistral(api_key = api_key)

response = mistral_client.chat.complete(
    model = "mistral-small-latest",
    messages = [
        {
            "role" : "user",
            "content" : "whats 5 times 7"
        }
    ]
)

print(response.choices[0].message.content)
