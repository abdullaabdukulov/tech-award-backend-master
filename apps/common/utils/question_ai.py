import requests
from googletrans import Translator


def translate_text(text, source_lang, target_lang):
    # Create a Translator object
    translator = Translator()

    # Detect the source language of the text
    detected_language = translator.detect(text).lang

    # Check if the source language matches the provided source_lang
    if detected_language != source_lang:
        raise ValueError(
            f"Detected language ({detected_language}) doesn't match the source language ({source_lang})."  # noqa
        )

    # Translate the text to the target language
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)

    return translated_text.text


api_ley = "8y1DBWfrL4ldA4GSmPh4w2rEMixF2kBM"
url = "https://api.ai21.com/studio/v1/j2-mid/complete"


def ai_response(prompt):
    payload = {
        "numResults": 1,
        "maxTokens": 8192,
        "minTokens": 0,
        "temperature": 1,
        "topP": 1,
        "topKReturn": 0,
        "frequencyPenalty": {
            "scale": 0,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True,
        },
        "presencePenalty": {
            "scale": 0,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True,
        },
        "countPenalty": {
            "scale": 0,
            "applyToWhitespaces": True,
            "applyToPunctuations": True,
            "applyToNumbers": True,
            "applyToStopwords": True,
            "applyToEmojis": True,
        },
        "prompt": prompt,
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer 8y1DBWfrL4ldA4GSmPh4w2rEMixF2kBM",
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    return data["completions"][0]["data"]["text"]
