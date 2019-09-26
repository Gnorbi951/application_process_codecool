import data_manager
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/name_of_all_mentors')
def mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_all_mentor_names()

    return render_template('mentor_names.html', mentor_names=mentor_names)


@app.route('/miskolc_mentor_nicknames')
def miskolc_mentor_nicknames():
    nicknames = data_manager.get_mentor_nicknames('Miskolc')

    return render_template('mentor_names.html', nicknames=nicknames)


if __name__ == '__main__':
    app.run(debug=True)