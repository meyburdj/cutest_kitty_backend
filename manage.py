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
        cat_creation_prompt='generate an image of a cat',
        cat_vision_prompt='''You are a professional cat-cuteness judge. You are judging cat's at the most prestigious competition for cat cuteness in the world. The stakes are high so your judgement must be precise. Rate this cat's cuteness on an integer scale of 1-100. Reply with only the integer grade value.'''
    )
    db.session.add(cat_group)
    db.session.commit()

    # Now the cat_group has an ID, we can create Cats and reference it
    cats = [
        Cat(url='https://cdn.discordapp.com/attachments/1233394404681846784/1233394465876607107/file-3eA7SfA07SCszv41sFrmQi1X.png?ex=662cef9c&is=662b9e1c&hm=290860919dce31050289b0519a7b4bc0691bdb31ae619ef0a9ec0065b074bb65&', 
            score=95, cat_group_id=cat_group.id),
        Cat(url='https://cdn.discordapp.com/attachments/1233394404681846784/1233395167248252948/file-elgiENZ3gxahU3dwZoiG0mqw.png?ex=662cf043&is=662b9ec3&hm=1f030467683f18c8fa2c2631ad976a740292c8deb36b4567534efd46dbcee07c&', 
            score=90, cat_group_id=cat_group.id),
        Cat(url='https://cdn.discordapp.com/attachments/1233394404681846784/1233397463319052298/file-wxvNpzxBNTLM201rsATCWpRx.png?ex=662cf266&is=662ba0e6&hm=ae1819e0048374f1538b98d6298c5ae5d77dea066aea1b7b832de149ac44644b&', 
            score=92, cat_group_id=cat_group.id),
        Cat(url='https://cdn.discordapp.com/attachments/1233394404681846784/1233398167924375552/file-JtYRnHtqvwAurN3ZrirTaNoN.png?ex=662cf30e&is=662ba18e&hm=670c58031a2ad9ed4d60b045b9b25796dffce336ef774b9649a29bfbd8a8d9eb&', score=95, cat_group_id=cat_group.id),
        Cat(url='https://cdn.discordapp.com/attachments/1233394404681846784/1233399415293612073/file-92xqDLbfwuhIIdynb44EtHRI.png?ex=662cf438&is=662ba2b8&hm=f4c3b36e60bf56554b49e6f50120aae69520c35012a2656168caf0bc4097b452&', score=85, cat_group_id=cat_group.id),
    ]
    db.session.add_all(cats)
    db.session.commit()
    
    click.echo(f"Added {len(cats)} cats to database under group ID {cat_group.id}.")

if __name__ == "__main__":
    cli()
    app.run(threaded=True)

