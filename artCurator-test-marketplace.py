from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

version = "0.0.2"
input_data = {
    "art_theme": "Fantasy",
    "style": "Surrealism",
    "medium": "Digital"
}

# If no version is provided it'll use the latest version by default
if version:
    flow_name = f"venmus/ai-art-curator/{version}"
else:
    flow_name = "venmus/ai-art-curator"

result = client.flow.execute(flow_name, input_data)
print(result)
