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
def get_miskolc_mentor_nicknames(cursor):
    cursor.execute("""
                    SELECT nick_name FROM mentors
                    WHERE city = 'Miskolc'
                    ORDER BY nick_name;
                    """,)
    nicknames = cursor.fetchall()
    return nicknames
