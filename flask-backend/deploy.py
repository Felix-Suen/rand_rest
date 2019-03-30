
from random import choice

from flask import Flask, render_template, redirect, request, url_for
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def restaurant():
    rest_lst = ['Mcdonalds', 'KFC', 'BurgerKing', 'Subway', 'Pizza Hut']
    if request.method == 'POST':
        return redirect(url_for('restaurant'))
    random = choice(rest_lst)
    return render_template('index.html', token=random)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)