import asyncio
from flask_restx import  Namespace, Resource
from flask import request, Response
from src.api.cats.crud import read_all_cat_ratings, create_group_and_cats
from src.api.cats.schemas import CatRatingResponse, CatGroup, CatData, NewCatData
from flask import jsonify


cats_namespace = Namespace("cats")

class CatRatingsList(Resource):
    def get(self):
        """Returns all cat ratings with images."""
        cat_ratings = read_all_cat_ratings()
        response = CatRatingResponse(groups=cat_ratings)
        response_json = response.json()
        return Response(response_json, mimetype='application/json', status=200)


    def post(self):
        """Generates 10 cat images, ranks them, stores them in the DB, and returns the group."""
        post_data = request.get_json()

        cat_creation = post_data.get("cat_creation")
        print('cat_creation in views', cat_creation)
        cute_vision = post_data.get("cute_vision")  
        print('cute_vision in views', cute_vision)      

        try:
            cat_ratings = create_group_and_cats(cat_creation_prompt=cat_creation, 
                                          cat_vision_prompt=cute_vision )
            print('cat_ratings in view', cat_ratings)
            response_model = CatRatingResponse(groups=[cat_ratings]) 
            response_model_json = response_model.json()

            return Response(response_model_json, mimetype='application/json', status=201)
        except Exception as e:
            cats_namespace.abort(500, f"Failed to process images due to {str(e)}")

cats_namespace.add_resource(CatRatingsList, "")
