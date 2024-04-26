from sqlalchemy.sql import func

from flask import current_app

from src import db

class Cat(db.Model):
    __tablename__="cats"

    id=db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    url = db.Column(
        db.String,
        unique=True,
        nullable=False
    )

    score = db.Column(
        db.Integer,
        nullable=False
    )

    cat_group_id=db.Column(
        db.Integer,
        db.ForeignKey('cat_groups.id'),
        nullable=False
    )

    def __init__(self, url, score, cat_group_id):
        self.url = url
        self.score = score
        self.cat_group_id = cat_group_id

class CatGroup(db.Model):
    __tablename__="cat_groups"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    creation_date = db.Column(
        db.DateTime,
        default=func.now(),
        nullable=False
    )

    cat_creation_prompt = db.Column(
        db.String,
        unique=False,
        nullable=False
    )

    cat_vision_prompt = db.Column(
        db.String,
        unique=False,
        nullable=False
    )


    cats = db.relationship('Cat', backref='cat_group', lazy=True)

    def __init__(self, creation_date, cat_creation_prompt, cat_vision_prompt):
        self.creation_date=creation_date
        self.cat_creation_prompt=cat_creation_prompt
        self.cat_vision_prompt=cat_vision_prompt
