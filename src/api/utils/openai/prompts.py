def generate_image_prompt(cat_creation_prompt_details):
    print('cat_creation_prompt_details', cat_creation_prompt_details)
    prompt_parts = ['a cat']

    # Add descriptive details based on user selections
    if cat_creation_prompt_details.get('size'):
        prompt_parts.append(f"that is {cat_creation_prompt_details['size']}")
        
    if cat_creation_prompt_details.get('breed'):
        prompt_parts.append(f"of {cat_creation_prompt_details['breed']} breed")
        
    if cat_creation_prompt_details.get('style'):
        prompt_parts.append(f"with a {cat_creation_prompt_details['style']} style")

    if len(prompt_parts) > 1:
        prompt = f"Generate an image of {' '.join(prompt_parts)}"
    else:
        prompt = f"Generate an image of {prompt_parts[0]}"

    return prompt

def analyze_image_prompt(cat_analyze_prompt_details):
    print('cat_analyze_prompt_details', cat_analyze_prompt_details)
    prompt_base = (
        "You are a professional cat-cuteness judge at the most prestigious competition for cat "
        "cuteness in the world. The stakes are high, and your judgment must be precise. "
    )
    
    detail_sentence = ""
    if cat_analyze_prompt_details.get('cutenessDefiners'):
        definers_list = ', '.join(cat_analyze_prompt_details['cutenessDefiners'])
        last_comma = definers_list.rfind(",")
        if last_comma != -1:
            definers_list = f"{definers_list[:last_comma]} and{definers_list[last_comma + 1:]}"
        
        detail_sentence = f"When judging cuteness, prioritize attributes such as {definers_list}. "
    
    prompt = f"{prompt_base}{detail_sentence}Rate this cat's cuteness on an integer scale of 1-100. Reply with only the integer grade value."
    
    return prompt
