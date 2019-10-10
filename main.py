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


@app.route('/search-for-applicant-by-first-name', methods=['GET', 'POST'])
def search_for_applicant_by_name():
    if request.method == 'GET':
        return render_template('applicant_by_first_name.html')
    else:
        first_name = request.form['searched_applicant']
        name_and_phone = data_manager.get_applicant_by_first_name(first_name)
        return render_template('applicant_by_first_name.html', name_and_phone=name_and_phone)


@app.route('/search-for-applicant-by-email', methods=['GET', 'POST'])
def search_for_applicant_by_email():
    if request.method == 'GET':
        return render_template('applicant_by_email.html')
    else:
        email = request.form['searched_email']
        found_emails = data_manager.get_applicant_by_email(email)
        return render_template('applicant_by_email.html', found_emails=found_emails)


@app.route('/add-new-applicant', methods=['GET', 'POST'])
def add_new_applicant():
    if request.method == 'GET':
        return render_template('add_new_applicant.html')
    else:
        applicant_info = [request.form['first_name'], request.form['last_name'],
                          request.form['phone_number'], request.form['email_address'],
                          request.form['application_code']]
        data_manager.adding_new_applicant(applicant_info)
        status = 'Applicant was successfully added'
        return render_template('add_new_applicant.html', status=status)


@app.route('/update-applicant-phone-number', methods=['GET', 'POST'])
def update_phone():
    if request.method == 'GET':
        return render_template('update-phone-number.html')
    else:
        applicant_info = [request.form['full_name'], request.form['phone_number']]
        data_manager.update_phone_number(applicant_info)
        return render_template('update-phone-number.html')


@app.route('/delete-applicant-by-email', methods=['GET', 'POST'])
def delete_applicant():
    if request.method == 'GET':
        return render_template('delete_applicant_by_email.html')
    else:
        email = request.form.get('email')
        data_manager.delete_applicant_by_email(email)
        return render_template('delete_applicant_by_email.html')


@app.route('/mentors')
def mentors_and_schools():
    mentor_info = data_manager.get_mentors_with_schools()
    return render_template('mentor_schools.html', mentor_info=mentor_info)


@app.route('/all-school')
def all_school_page():
    all_school_info = data_manager.get_mentors_with_all_schools()
    return render_template('mentor_with_all_schools.html', all_school_info=all_school_info)


@app.route('/mentors-by-country')
def mentors_by_country():
    country_info = data_manager.get_mentor_number_per_country()
    return render_template('mentor_per_country.html', country_info=country_info)


@app.route('/contacts')
def contacts():
    contact_info = data_manager.get_contact_person()
    return render_template('contact_people.html', contact_info=contact_info)


@app.route('/applicants')
def applicants():
    applicant_info = data_manager.get_applicant_info()
    return render_template('applicant_info.html', applicant_info=applicant_info)


if __name__ == '__main__':
    app.run(debug=True)
