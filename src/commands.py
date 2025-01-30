from flask.cli import with_appcontext
import click
from .extensions import db
from .models.chat import ChatRoom

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Initializing Database")

    db.drop_all()
    db.create_all()

    click.echo("Database Created")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Populating database")
    new_room = ChatRoom(id=1, name="Room1")
    db.session.add(new_room)
    db.session.commit()
    click.echo("Populated db")


def init_test_db():
    db.create_all()

    for i in range(0, 3):
        new_room = ChatRoom(name=f"testroomg{i}")
        db.session.add(new_room)
    db.session.commit()


