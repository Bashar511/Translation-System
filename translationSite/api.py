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
    
def bart_en2ar(payload):
    #headers = {"Authorization": f"Bearer {API_TOKEN}"}
    API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
    #data = json.dumps(payload)
    med = {"inputs": payload, "parameters": {"src_lang": "en_XX", "tgt_lang": "ar_AR"}}
    data = json.dumps(med)
    response = requests.request("POST", API_URL, data=data)
    if response.ok:
        text = json.loads(response.content.decode("utf-8"))
        return text[0]['translation_text']
    else:
        return response.reason