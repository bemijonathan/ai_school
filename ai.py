import os
import base64
import requests

api_key = os.getenv('OPENAI_API_KEY')
model = "gpt-4-turbo"

print(api_key, "________")
def convert_to_base64(image):
    with open(image, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def explain_power_point_image(images):
    base64_images = []
    for image in images:
        base64_images.append(convert_to_base64(image))

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    for image in base64_images[0:2]:
        payload = {
            "model": "gpt-4-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are a professor your role is to explain the content of the slide"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    print(response.json())
