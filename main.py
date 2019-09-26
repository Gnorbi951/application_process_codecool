import data_manager
from flask import Flask, render_template, request

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


@app.route('/search-for-applicant', methods=['GET', 'POST'])
def search_for_applicant():
    if request.method == 'GET':
        return render_template('applicant_by_first_name.html')
    else:
        first_name = request.form['searched_applicant']
        name_and_phone = data_manager.get_applicant_by_first_name(first_name)
        return render_template('applicant_by_first_name.html', name_and_phone=name_and_phone)


if __name__ == '__main__':
    app.run(debug=True)
