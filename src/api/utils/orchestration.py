import asyncio
from src.api.utils.openai.calls import generate_image, analyze_image

async def generate_and_analyze_cats(cat_creation_prompt, cat_vision_prompt):
    # Generate 5 cat images using the same prompt concurrently
    image_tasks = [generate_image(cat_creation_prompt) for _ in range(2)]
    images = await asyncio.gather(*image_tasks)
    print('images: ', images)

    # Analyze each image for cuteness
    analysis_tasks = [analyze_image(image, cat_vision_prompt) for image in images]
    analysis_results = await asyncio.gather(*analysis_tasks)
    print('analysis_results: ', analysis_results)

    # Combine image data with analysis results
    cat_data = [{"url": image, "score": result} for image, result in zip(images, analysis_results)]
    print('cat_data in orchest', cat_data)
    return cat_data

def orchestrate_cat_creation_and_analysis(cat_creation_prompt, cat_vision_prompt):
    return asyncio.run(generate_and_analyze_cats(cat_creation_prompt, cat_vision_prompt))
