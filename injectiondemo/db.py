import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """Create Postgres connection"""

    if 'db' not in g:
        g.db = psycopg2.connect(
            f"dbname={current_app.config['DATABASE']}"
        )

    return g.db


def close_db(e=None):
    """Close Postgres connection"""

    db = g.pop('db', None)

    if db is not None:
        db.close()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Create and populate database tables"""
    
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        with db.cursor() as cur:
            cur.execute(f.read().decode('utf8'))
            db.commit()

    click.echo('Initialized the database.')


