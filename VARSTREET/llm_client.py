"""Utility to interact with an LLM provider."""
from mistralai import Mistral
import os
from temp_vars.knowledge_base import filter_operators
from temp_vars.prompt_store import prompt_part1,prompt_part2,prompt_part3 
from utils import extract_valid_json,get_filter_options_by_screenURL

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
        api_key = os.getenv("MISTRAL_API_KEY")
        if not api_key:
            raise ValueError("API key not found in environment variable 'MISTRAL_API_KEY'")

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


def callAdvancedFilter(user_question,screenURL):
    filter_options = get_filter_options_by_screenURL(screenURL)
    prompt = prompt_part1.format(filter_options=filter_options,operators=filter_operators) + prompt_part2 + prompt_part3.format(query=user_question)
    response = callGenAIAPI(prompt)
    json_response = extract_valid_json(response)
    return json_response