import requests

GEMINI_API_KEY = "your api here"  # Replace with your Google AI API Key

def get_gemini_response(user_message):
    """Fetches AI-generated response from Gemini API"""
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [{"role": "user", "parts": [{"text": f"Give a concise, friendly response: {user_message}"}]}],
        "generationConfig": {
            "maxOutputTokens": 100,  # Prevents cut-off responses
            "temperature": 0.7
        }
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response_json = response.json()

        bot_reply = (
            response_json.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "Sorry, I couldn't generate a response.")
        )
        return bot_reply.strip()

    except Exception as e:
        print("API Error:", str(e))
        return "I'm facing some issues. Please try again later."
