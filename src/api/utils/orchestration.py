import os
import asyncio
from src.api.utils.openai.calls import generate_image, analyze_image
from src.api.utils.aws.s3 import upload_image_to_s3

async def generate_and_analyze_cats(cat_creation_prompt, cat_vision_prompt):
    # Generate cat images concurrently
    # image_tasks = [asyncio.create_task(generate_image(cat_creation_prompt)) for _ in range(2)]
    images = await asyncio.gather(*[generate_image(cat_creation_prompt) for _ in range(2)])
    print('images', images)
    s3_urls = [upload_image_to_s3(image, os.getenv("BUCKET_NAME"), 'cats') for image in images]
    print('s3_urls', s3_urls)

    # Analyze each image for cuteness concurrently
    analysis_tasks = [asyncio.create_task(analyze_image(s3_url, cat_vision_prompt)) for s3_url in s3_urls]
    analysis_results = await asyncio.gather(*analysis_tasks)

    # Combine image data with analysis results
    cat_data = [{"url": image, "score": result} for image, result in zip(s3_urls, analysis_results)]
    return cat_data
