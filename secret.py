import psycopg2


# Reading of secret key for password file
def connect():
    connection = psycopg2.connect(
        host="localhost",
        database="matthewjoseph"
    )
    return connection


def get_master_pwd():
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM master_info """
        cursor.execute(postgres_select_query)
        connection.commit()
        result = cursor.fetchone()
        return result[0]
    except (Exception, psycopg2.Error) as error:
        print(error)


get_master_pwd()
