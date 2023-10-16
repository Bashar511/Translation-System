import json
import requests


def hel_en2ar(payload):
    #headers = {"Authorization": f"Bearer {API_TOKEN}"}
    API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-tc-big-en-ar"
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, data=data)
    if response.ok:
        text = json.loads(response.content.decode("utf-8"))
        return text[0]['translation_text']
    else:
        return response.reason