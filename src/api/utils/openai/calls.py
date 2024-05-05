from openai import AsyncOpenAI
from src.api.utils.openai.config import get_openai_key

async def generate_image(cat_creation_prompt):
    api_key = get_openai_key()
    client = AsyncOpenAI(api_key=api_key)
    print('im in generate_image', cat_creation_prompt)
    response =  await client.images.generate(
    model="dall-e-3",
    prompt=cat_creation_prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    )
    print('response', response)
    image_url = response.data[0].url
    print('image_url', image_url)
    return image_url

async def analyze_image(image_url, cat_analyze_prompt):
    api_key = get_openai_key()
    client = AsyncOpenAI(api_key=api_key)
    response =  await client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": cat_analyze_prompt},
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
    choice= response.choices[0]
    content = choice.message.content
    print('content: ', content)
    return content
