import openai
from src.api.utils.openai.config import get_openai_key
from src.api.utils.openai.prompts import generate_image_prompt, analyze_image_prompt


async def generate_image(cat_creation_prompt_details):
    prompt = generate_image_prompt(cat_creation_prompt_details)
    api_key = get_openai_key()
    openai.api_key = api_key
    response = openai.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
    return image_url

async def analyze_image(image_url, cat_analyze_prompt_details):
    prompt = analyze_image_prompt(cat_analyze_prompt_details)
    api_key = get_openai_key()
    openai.api_key = api_key
    response = openai.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {
            "type": "image_url",
            "image_url": {
                "url": image_url,
            },
            },
        ],
        }
    ],
    max_tokens=1,
    )

    print(response.choices[0])
