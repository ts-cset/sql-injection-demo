import os
import sqlite3

from flask import Flask, request, render_template


def create_app(test_config=None):
    """Application factory"""

    # Create the application
    app = Flask(__name__, instance_relative_config=True)

    # Configure the app for each environment
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'injectiondemo.sqlite')
    )
    if test_config is not None:
        app.config.from_mapping(test_config)

    # Setup instance folder for SQLite database file
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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
            try:
                results = db.get_db().execute(
                    "SELECT name, price, quantity FROM products"
                    " WHERE name LIKE '%" + query + "%'"
                ).fetchall()
            except sqlite3.OperationalError as sql_error:
                print(sql_error)
                error = 'Sorry, something went wrong...'

            return render_template('search.html', query=query, results=results, error=error)

        return render_template('search.html')

    return app

