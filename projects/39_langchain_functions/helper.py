# Simple helper function for pretty printing
import json
from pprint import pprint


def show_response(response):
    """Display OpenAI response in a readable format."""
    try:
        if hasattr(response, "model_dump"):
            data = response.model_dump()
            print(json.dumps(data, indent=2))
        else:
            pprint(response)
    except Exception as e:
        print(f"Error displaying response: {e}")
        print(response)