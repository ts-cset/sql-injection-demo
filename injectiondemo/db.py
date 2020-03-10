import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """Create SQLite connection"""

    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

    return g.db


def close_db(e=None):
    """Close SQLite connection"""

    db = g.pop('db', None)

    if db is not None:
        db.close()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Create and populate database tables"""

    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    click.echo('Initialized the database.')


