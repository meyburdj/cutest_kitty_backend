import asyncio
from flask_restx import  Resource
from flask import request
from src.api.utils.orchestration import orchestrate_cat_ratings
from src.api.cats.crud import read_all_cat_ratings, create_group_and_cats
from src.api.cats.schemas import CatRatingResponse, ImageData, ImageGroup


class CatRatingsList(Resource):
    def get(self):
        """Returns all cat ratings with images."""
        cat_ratings = read_all_cat_ratings()  
        return CatRatingResponse(groups=cat_ratings).json(), 200


    def post(self):
        """Generates 10 cat images, ranks them, stores them in the DB, and returns the group."""
        post_data = request.get_json()

        cat_creation = post_data.get("cat_creation")
        cute_vission = post_data.get("cute_vission")        

        try:
            cat_ratings = create_group_and_cats(cat_creation_prompt=cat_creation, 
                                          cat_vission_prompt=cute_vission )
            return cat_ratings, 201
        except Exception as e:
            cats_namespace.abort(500, f"Failed to process images due to {str(e)}")

cats_namespace.add_resource(CatRatingsList, "")
