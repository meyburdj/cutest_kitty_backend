import click
from flask import Flask
from flask.cli import FlaskGroup
from src import create_app, db
from src.api.cats.models import Cat, CatGroup

app = create_app()
cli = FlaskGroup(create_app=lambda: app)

@cli.command('recreate_db')
def recreate_db():
    """Drops and recreates the database."""
    db.drop_all()
    db.create_all()
    db.session.commit()
    click.echo("Database recreated!")

@cli.command('seed_group_and_cats')
def seed_group_and_cats():
    """Seeds the database with a cat group and some cats."""
    # Create and commit the CatGroup to ensure it has an ID
    cat_group = CatGroup(
        cat_creation_prompt='this is a test cat_creation_prompt',
        cat_vision_prompt='this is a test cat_vision_prompt'
    )
    db.session.add(cat_group)
    db.session.commit()

    # Now the cat_group has an ID, we can create Cats and reference it
    cats = [
        Cat(url='http://example.com/test_url_1', score=5, cat_group_id=cat_group.id),
        Cat(url='http://example.com/test_url_2', score=1, cat_group_id=cat_group.id),
        Cat(url='http://example.com/test_url_3', score=2, cat_group_id=cat_group.id),
        Cat(url='http://example.com/test_url_4', score=6, cat_group_id=cat_group.id),
        Cat(url='http://example.com/test_url_5', score=8, cat_group_id=cat_group.id),
    ]
    db.session.add_all(cats)
    db.session.commit()
    click.echo(f"Added {len(cats)} cats to database under group ID {cat_group.id}.")

if __name__ == "__main__":
    cli()
