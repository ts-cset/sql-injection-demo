import os
import sqlite3

from flask import Flask, request, render_template


def create_app(test_config=None):
    """Application factory"""

    # Create the application
    app = Flask(__name__, instance_relative_config=True)

    # Configure the app for each environment
    app.config.from_mapping(DATABASE='injectiondemo')
    if test_config is not None:
        app.config.from_mapping(test_config)

    # Register database hooks
    from . import db
    app.teardown_appcontext(db.close_db)
    app.cli.add_command(db.init_db_command)

    # Register routes
    @app.route('/', methods=('GET', 'POST'))
    def index():
        if request.method == 'POST':
            query = request.form['query']
            error = None
            results = []

            # get results from db
            with db.get_db().cursor() as cur:
                try:
                    sql = f"""
                        SELECT name, price, quantity FROM products
                        WHERE name ILIKE '%{query}%'
                    """
                    cur.execute(sql)
                    results = cur.fetchall()
                except Exception as sql_error:
                    print(sql_error)
                    error = 'Sorry, something went wrong...'

            return render_template('search.html', query=query, results=results, error=error)

        return render_template('search.html')

    return app

