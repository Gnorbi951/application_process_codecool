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
