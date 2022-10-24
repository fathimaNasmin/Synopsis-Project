from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


@app.route('/')
def student():
    curr_year = date.today().year
    return render_template('index.html', year=curr_year)

@app.route('/evaluator')
def evaluator():
    return render_template('evaluator.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)

