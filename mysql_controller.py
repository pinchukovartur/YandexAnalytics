from MySQLdb import *

connection = connect(user='root',
                     passwd='root',
                     host='127.0.0.1',
                     db='world')


def get_all_events(connection):
    query = "SELECT * FROM analytics.events"
    connection.query(query)
    result = connection.store_result()
    list_row = list(result.fetch_row(result.num_rows()))
    return list_row


def insert_events(connection, inserts):


    query = "INSERT INTO analytics.events (android_id, event_datetime) VALUES ( '%s', '%s');"

    try:
        import datetime
        connection.cursor().execute(query, (1, datetime.date.today()))
        connection.commit()
    except MySQLError as error:
        print(error)
        connection.rollback()



insert_events(connection, "")