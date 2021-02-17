import psycopg2


# connections and queries
def connect():
    connection = psycopg2.connect(
        host="localhost",
        database="accountmanager"
    )
    return connection


def store_accountInfo(password, username, email, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """INSERT INTO account_info (password, username, email, app_name) VALUES (%s, %s, %s, 
        %s) """
        postgres_insert_values = (password, username, email, app_name)
        cursor.execute(postgres_insert_query, postgres_insert_values)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)


def searchByEmail(email):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM account_info WHERE email = '""" + email + "'"
        cursor.execute(postgres_select_query, email)
        connection.commit()
        result = cursor.fetchall()

        print('')
        print('RESULTS')
        print('')
        print(result)
        print('')
        print('-' * 30)
    except (Exception, psycopg2.Error) as error:
        print(error)


def searchByPassword(pwrd):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM account_info WHERE password = '""" + pwrd + "'"
        cursor.execute(postgres_select_query, pwrd)
        connection.commit()
        result = cursor.fetchall()

        print('')
        print('RESULTS')
        print('')
        print(result)
        print('')
        print('-' * 30)
    except (Exception, psycopg2.Error) as error:
        print(error)

