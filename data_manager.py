import database_common


@database_common.connection_handler
def get_all_mentor_names(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    ORDER BY first_name;
                   """, )
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


@database_common.connection_handler
def delete_applicant_by_email(cursor, email):
    cursor.execute("""
                        DELETE FROM applicants
                        WHERE email LIKE %(email)s
                        """,
                   {'email': f'%{email}'})


@database_common.connection_handler
def get_mentors_with_schools(cursor):
    cursor.execute("""
                    SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                    FROM mentors
                        INNER JOIN schools
                        ON mentors.city = schools.city
                        ORDER BY mentors.id;
                    """)
    mentor_info = cursor.fetchall()
    return mentor_info


@database_common.connection_handler
def get_mentors_with_all_schools(cursor):
    cursor.execute("""
                    SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                    FROM mentors
                        RIGHT JOIN schools
                        ON mentors.city = schools.city
                    ORDER BY mentors.id
                    """)
    all_school_info = cursor.fetchall()
    return all_school_info


@database_common.connection_handler
def get_mentor_number_per_country(cursor):
    cursor.execute("""
                        SELECT country, COUNT(mentors.id) AS mentors FROM mentors
                            FULL JOIN schools 
                                ON mentors.city = schools.city
                        GROUP BY country
                        ORDER BY country;
                    """)
    country_info = cursor.fetchall()
    return country_info


@database_common.connection_handler
def get_contact_person(cursor):
    cursor.execute("""
                    SELECT schools.name, mentors.first_name, mentors.last_name FROM mentors
                    INNER JOIN schools
                        ON mentors.id = schools.contact_person
                    ORDER BY schools.name;
                    """)
    contact_info = cursor.fetchall()
    return contact_info


@database_common.connection_handler
def get_applicant_info(cursor):
    cursor.execute("""
                    SELECT applicants.first_name, applicants.application_code, creation_date FROM applicants
                    INNER JOIN applicants_mentors
                        ON  applicants.id = applicants_mentors.applicant_id
                    WHERE creation_date > '2016-01-01'
                    ORDER BY creation_date DESC;
                    """)
    applicant_info = cursor.fetchall()
    return applicant_info


@database_common.connection_handler
def get_applicants_mentors(cursor):
    cursor.execute("""
                        SELECT applicants.first_name AS "ap_first_name",
                        applicants.application_code, mentors.first_name AS "me_first_name", mentors.last_name 
                        FROM applicants
                        FULL JOIN applicants_mentors
                            ON applicants.id = applicants_mentors.applicant_id
                        LEFT JOIN mentors
                            ON mentors.id = applicants_mentors.mentor_id;
                        """)
    applicants_mentors = cursor.fetchall()
    return applicants_mentors