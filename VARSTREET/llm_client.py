"""Utility to interact with an LLM provider."""
from mistralai import Mistral
import os
from temp_vars.knowledge_base import KNOWLEDGE_BASE
from temp_vars.prompt_store import ADVANCED_FILTER_PROMPT 
from utils import extract_valid_json

def callGenAIAPI(prompt: str) -> str:
    """Call the API with the given prompt and return the response.

    Parameters
    ----------
    prompt : str
        The prompt to send to the model.

    Returns
    -------
    str
        The assistant's reply if successful, or an error message.
    """
    try:
        api_key = os.getenv("MISTRAL_API_KEY_CALL_BOT")
        if not api_key:
            raise ValueError("API key not found in environment variable 'MISTRAL_API_KEY_CALL_BOT'")

        model = "mistral-large-latest"
        client = Mistral(api_key=api_key)

        chat_response = client.chat.complete(
            model=model,
            messages=[
                {"role": "user", "content": prompt},
            ]
        )

        return chat_response.choices[0].message.content

    except Exception as e:
        return f"❌ Error during API call: {str(e)}"


def callAdvancedFilter(user_question,json_id):
    knowledge = KNOWLEDGE_BASE[json_id]["advancedFilter"]
    prompt = ADVANCED_FILTER_PROMPT #TODO : add user question and knowledge to the prompt.
    response = callGenAIAPI(prompt)
    json_response = extract_valid_json(response)
    return json_response