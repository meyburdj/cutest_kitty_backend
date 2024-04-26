import asyncio
from src.api.utils.openai.calls import generate_image, analyze_image

async def generate_and_analyze_cats(cat_creation_prompt, cat_vision_prompt):
    # Generate 5 cat images using the same prompt concurrently
    image_tasks = [generate_image(cat_creation_prompt) for _ in range(5)]
    images = await asyncio.gather(*image_tasks)

    # Analyze each image for cuteness
    analysis_tasks = [analyze_image(image['url'], cat_vision_prompt) for image in images]
    analysis_results = await asyncio.gather(*analysis_tasks)

    # Combine image data with analysis results
    cat_data = [{"url": image['url'], "analysis": result} for image, result in zip(images, analysis_results)]

    return cat_data

def orchestrate_cat_creation_and_analysis(cat_creation_prompt, cat_vision_prompt):
    # Run the async generate and analyze function
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(
        generate_and_analyze_cats(cat_creation_prompt, cat_vision_prompt)
    )