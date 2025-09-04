import json
import re
import os
import requests

def extract_valid_json(text: str):
    """
    Extracts and validates JSON from LLM-generated text.
    
    Args:
        text (str): Raw output from LLM which may contain JSON.
    
    Returns:
        dict: Parsed JSON object if extraction and validation is successful.

    Raises:
        ValueError: If no valid JSON could be extracted or parsed.
    """
    try:
        # Try direct parse first (if pure JSON string)
        return json.loads(text)
    except:
        try:
            return json.loads(text[text.index("{"):text.rindex("}")+1])
        except Exception as e:
            return f"❌ Error converting LLM-generated text to JSON LLM-TEXT{text}\nerror: {str(e)}"
        
def get_filter_options_by_screenURL(screenURL: str):
    """
    """
    try:
        url = os.getenv("VARSTREET_SCREENURL")#"https://procode-363409.uc.r.appspot.com/api/screen/getInDraftScreenByURL"
        data = {"screenURL":screenURL}
        response = requests.post(url, json=data)
        result_data = response.json()
        if result_data != None:
            data = [each_dict for each_dict in result_data['data'] if "#list" in each_dict["screenURL"]]
            return json.loads(data[0]['screenMetadata'])['advancedFilter']
        else:
            return "Check the provided ScreenURL."
    except Exception as e:
        return f"❌ Error in fetching the filter options data\nerror: {str(e)}"
