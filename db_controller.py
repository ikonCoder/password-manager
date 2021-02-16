import psycopg2


# connections and queries
def connect():
    connection = psycopg2.connect(
        host="localhost",
        database="matthewjoseph"
    )
    return connection


def store_username():
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM master_info """
        cursor.execute(postgres_select_query)
        connection.commit()
        result = cursor.fetchone()
        print('Password is: ')
        print(result[0])
    except (Exception, psycopg2.Error) as error:
        print(error)

