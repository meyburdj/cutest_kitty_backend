from src import db
from src.api.cats.models import Cat, CatGroup
from src.api.utils.orchestration import orchestrate_cat_ratings

def create_group_and_cats(cat_creation_prompt, cat_vission_prompt):
    '''takes prompts. creates group and cats associated with that group. returns
    dictionary representation of cats group'''
    cat_group = create_cat_rating_group(cat_creation_prompt=cat_creation_prompt,
                                       cat_vission_prompt=cat_vission_prompt)
    cats = create_cat_ratings(cat_group)
    return cats

def create_cat_rating_group(cat_creation_prompt, cat_vision_prompt):
    '''creates a new cat_rating_group record with a creation time and id'''
    cat_group = CatGroup()
    db.session.add(cat_group)
    db.session.flush()

def create_cat_ratings(rating_group):
    '''creates a new cat record with a url and score'''
    cats = orchestrate_cat_ratings()
    for cat in cats:
        new_cat = Cat(url=img['url'], score=img['score'], cat_group_id=rating_group)
        db.session.add(new_cat)

    db.session.commit()

def read_all_cat_ratings():
    '''returns a list of lists of dicts i.e. [[{}, {}, {}], [{}, {}, {}]...]'''

def read_cat_ratings():
    '''returns a list of dictionaries grouped by cat_rating_id'''



