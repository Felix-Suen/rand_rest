from random import choice

from flask import (Flask, render_template, request, redirect, url_for)

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=('GET', 'POST'))
    def hello():
        if request.method == 'POST':
            return redirect(url_for('rest'))
        return render_template('index.html')

    @app.route('/rest', methods=('GET', 'POST'))
    def rest():
        rest_lst = ['Mcdonalds', 'KFC', 'BurgerKing', 'Subway', 'Pizza Hut']
        if request.method == 'POST':
            return redirect(url_for('rest'))
        random = choice(rest_lst)
        return render_template('rest.html', token=random)

    return app

if __name__ == '__main__':
    create_app()
