
import requests


def emotion_detector(text_to_analyze):
    """Analyze text and return scores for the five emotions."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=input_json,
        timeout=30
    )

    result = response.json()
    emotions = result["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion

    return emotions
