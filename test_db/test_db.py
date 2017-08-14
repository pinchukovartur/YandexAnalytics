from MySQLdb import *

""" Class to Create Test Select In DB"""


# ---------------------------------------------------------------------
# Program by Pinchukov Artur
#
# Version     Data      Info
#  1.0     14.08.2017
# ---------------------------------------------------------------------

def select(user, password, host, db, query):
    connection = connect(user=user,
                         passwd=password,
                         host=host,
                         db=db)
    connection.query(query)
    result = connection.store_result()
    list_row = list(result.fetch_row(result.num_rows()))
    print(len(list_row))
    return list_row


"""Тестовый запрос, который выводит все записи из установок и событий с одинаковым android_id, в городе Yekaterinburg 
и с событием Task """
query = "SELECT * FROM analytics.installations, analytics.events WHERE " \
        "installations.city = 'Yekaterinburg' and events.event_name = 'Task';"


select("root", "root", "127.0.0.1", "analytics", query)