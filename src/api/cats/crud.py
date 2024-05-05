from src import db
from src.api.cats.models import Cat, CatGroup
from src.api.utils.orchestration import generate_and_analyze_cats
from sqlalchemy.orm import joinedload
from src.api.utils.openai.prompts import generate_image_prompt, analyze_image_prompt
from src.api.cats.schemas import CatData

async def create_group_and_cats(cat_creation_prompt, cat_vision_prompt):
    '''takes prompts. creates group and cats associated with that group. returns
    dictionary representation of cats group'''

    generate_prompt =  generate_image_prompt(cat_creation_prompt)
    analyze_prompt = analyze_image_prompt(cat_vision_prompt)
    cat_group = create_cat_rating_group(cat_creation_prompt=generate_prompt,
                                       cat_vision_prompt=analyze_prompt)
    cats = await create_cat_ratings(cat_group.id, generate_prompt, analyze_prompt )


    return {"id": cat_group.id, 
            "creation_date": cat_group.creation_date.isoformat(), 
            "cat_creation_prompt": cat_group.cat_creation_prompt, 
            "cat_vision_prompt": cat_group.cat_vision_prompt, 
            "cats": cats}

def create_cat_rating_group(cat_creation_prompt, cat_vision_prompt):
    '''creates a new cat_rating_group record with a creation time and id'''
    cat_group = CatGroup(cat_creation_prompt=cat_creation_prompt, 
                         cat_vision_prompt=cat_vision_prompt)
    
    db.session.add(cat_group)
    db.session.flush()

    return cat_group

async def create_cat_ratings(cat_group_id, cat_creation_prompt, cat_vision_prompt):
    '''creates a new cat record with a url and score'''
    cats = await generate_and_analyze_cats(cat_creation_prompt, cat_vision_prompt)
    for cat in cats:
        new_cat = Cat(url=cat['url'], score=cat['score'], cat_group_id=cat_group_id)
        db.session.add(new_cat)

    db.session.commit()

    return cats

def read_all_cat_ratings():
    '''returns a list of dicts i.e. [
        {cat_creation_prompt, cat_vision_prompt, cats: [{}, {}, {}], [{}, {}, {}], 
        {...},...]'''
    cat_groups = CatGroup.query.options(joinedload(CatGroup.cats)).all()
    
    # Organize data into a list of dictionaries
    cat_ratings = [
        {
            "id": group.id,
            "creation_date": group.creation_date.isoformat(),
            "cat_creation_prompt": group.cat_creation_prompt,
            "cat_vision_prompt": group.cat_vision_prompt,
            "cats": [
                {"url": cat.url, "score": cat.score} for cat in group.cats
            ]
        } for group in cat_groups
    ]
    return cat_ratings

def read_cat_ratings(cat_group_id):
    '''returns a list of dictionaries grouped by cat_rating_id'''



