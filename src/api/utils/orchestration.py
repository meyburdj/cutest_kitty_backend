import asyncio
from src.api.utils.openai.calls import generate_image, analyze_image

async def generate_and_analyze_cats(cat_creation_prompt, cat_vision_prompt):
    # Generate cat images concurrently
    # image_tasks = [asyncio.create_task(generate_image(cat_creation_prompt)) for _ in range(2)]
    images = await asyncio.gather(*[generate_image(cat_creation_prompt) for _ in range(2)])

    # Analyze each image for cuteness concurrently
    analysis_tasks = [asyncio.create_task(analyze_image(image, cat_vision_prompt)) for image in images]
    analysis_results = await asyncio.gather(*analysis_tasks)

    # Combine image data with analysis results
    cat_data = [{"url": image, "score": result} for image, result in zip(images, analysis_results)]
    return cat_data
