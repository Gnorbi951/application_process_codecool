import database_common


@database_common.connection_handler
def get_all_mentor_names(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    ORDER BY first_name;
                   """,)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_nicknames(cursor, city):
    cursor.execute("""
                    SELECT nick_name FROM mentors
                    WHERE city = %(city)s
                    ORDER BY nick_name;
                    """,
                   {'city': city})
    nicknames = cursor.fetchall()
    return nicknames


@database_common.connection_handler
def get_applicant_by_first_name(cursor, applicant):
    cursor.execute("""
                    SELECT full_name, phone_number FROM applicants
                    WHERE first_name = %(applicant)s;
                    """,
                   {'applicant': applicant})
    name = cursor.fetchall()
    return name


@database_common.connection_handler
def get_applicant_by_email(cursor, email):
    cursor.execute("""
                    SELECT full_name, phone_number, email FROM applicants
                    WHERE email LIKE %(email)s;
                    """,
                   {'email': f'%{email}%'})
    found_emails = cursor.fetchall()
    return found_emails


@database_common.connection_handler
def adding_new_applicant(cursor, applicant_info):
    first_name, last_name, phone_number, email, application_code, full_name = 0, 1, 2, 3, 4, 5
    full_name = applicant_info[first_name] + ' ' + applicant_info[last_name]
    largest_id = get_largest_id_from_applicants()
    current_id = (largest_id[0].get('max')) + 1
    cursor.execute("""
                    INSERT INTO applicants
                    VALUES(%(current_id)s, %(first_name)s, %(last_name)s,
                            %(phone_number)s, %(email)s, %(application_code)s, %(full_name)s);
                    """,
                   {'current_id': current_id,
                    'first_name': applicant_info[first_name],
                    'last_name': applicant_info[last_name],
                    'phone_number': applicant_info[phone_number],
                    'email': applicant_info[email],
                    'application_code': applicant_info[application_code],
                    'full_name': full_name})


@database_common.connection_handler
def get_largest_id_from_applicants(cursor):
    cursor.execute("""
                    SELECT MAX(id) FROM applicants;""")
    largest_id = cursor.fetchall()
    return largest_id


@database_common.connection_handler
def update_phone_number(cursor, applicant_info):
    applicants_full_name = applicant_info[0]
    new_number = applicant_info[1]
    cursor.execute("""
                        UPDATE applicants
                        SET phone_number = %(new_number)s
                        WHERE full_name = %(applicants_full_name)s;
                        """,
                   {'new_number': new_number,
                    'applicants_full_name': applicants_full_name})
