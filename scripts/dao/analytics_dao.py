from MySQLdb import *

""" Class to Create Connection Analytics DB and method of management"""


# ---------------------------------------------------------------------
# Program by Pinchukov Artur
#
# Version     Data      Info
#  1.0     11.08.2017
# ---------------------------------------------------------------------

class AnalyticsDB:
    """ The method init class and create connection with DB"""

    def __init__(self, user, password, host):
        self.connection = connect(user=user,
                                  passwd=password,
                                  host=host,
                                  db="analytics")

    """ The method return list row with events"""

    def get_all_events(self):
        query = "SELECT * FROM analytics.events"
        self.connection.query(query)
        result = self.connection.store_result()
        list_row = list(result.fetch_row(result.num_rows()))
        return list_row

    """ The method add event in DB"""

    def insert_events(self, event):

        query = "INSERT INTO analytics.events (android_id,app_package_name,app_version_name,appmetrica_device_id," \
                "city,connection_type,country_iso_code,device_locale,device_manufacturer,device_model,device_type," \
                "event_datetime,event_json,event_name,event_receive_datetime,event_receive_timestamp,event_timestamp," \
                "google_aid,ios_ifa,ios_ifv,mcc,mnc,operator_name,os_name,os_version) VALUES (%s, %s,%s, %s,%s, %s,%s," \
                " %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
        try:
            print(self._check_event(event))
            if self._check_event(event):
                self.connection.cursor().execute(query, (
                    event["android_id"], event["app_package_name"], event["app_version_name"],
                    event["appmetrica_device_id"],
                    event["city"], event["connection_type"], event["country_iso_code"], event["device_locale"],
                    event["device_manufacturer"], event["device_model"], event["device_type"], event["event_datetime"],
                    event["event_json"], event["event_name"], event["event_receive_datetime"],
                    event["event_receive_timestamp"],
                    event["event_timestamp"], event["google_aid"], event["ios_ifa"], event["ios_ifv"], event["mcc"],
                    event["mnc"], event["operator_name"], event["os_name"], event["os_version"]))

                self.connection.commit()
        except MySQLError as error:
            print(error)
            print(
                event["android_id"], event["app_package_name"], event["app_version_name"],
                event["appmetrica_device_id"],
                event["city"], event["connection_type"], event["country_iso_code"], event["device_locale"],
                event["device_manufacturer"], event["device_model"], event["device_type"], event["event_datetime"],
                event["event_json"], event["event_name"], event["event_receive_datetime"],
                event["event_receive_timestamp"],
                event["event_timestamp"], event["google_aid"], event["ios_ifa"], event["ios_ifv"], event["mcc"],
                event["mnc"], event["operator_name"], event["os_name"], event["os_version"])
            self.connection.rollback()

    """ This method checks if there is data in the database"""

    def _check_event(self, event):
        query = "SELECT * FROM analytics.events WHERE android_id=%s AND app_package_name=%s AND app_version_name=%s AND appmetrica_device_id=%s AND city=%s AND connection_type=%s AND country_iso_code=%s AND device_locale=%s AND device_manufacturer=%s AND device_model=%s AND device_type=%s AND event_datetime=%s AND event_json=%s AND event_name=%s AND event_receive_datetime=%s AND event_receive_timestamp=%s AND event_timestamp=%s AND google_aid=%s AND ios_ifa=%s AND ios_ifv=%s AND mcc=%s AND mnc=%s AND operator_name=%s AND os_name=%s AND os_version=%s"
        try:
            arg = (event["android_id"], event["app_package_name"], event["app_version_name"],
                event["appmetrica_device_id"],
                event["city"], event["connection_type"], event["country_iso_code"], event["device_locale"],
                event["device_manufacturer"], event["device_model"], event["device_type"], event["event_datetime"],
                event["event_json"], event["event_name"], event["event_receive_datetime"],
                event["event_receive_timestamp"],
                event["event_timestamp"], event["google_aid"], event["ios_ifa"], event["ios_ifv"], event["mcc"],
                event["mnc"], event["operator_name"], event["os_name"], event["os_version"])

            items_request = self.connection.cursor().execute(query, arg)
            print(items_request)
            if items_request == 0:
                return True
            else:
                return False
        except MySQLError as error:
            print(error)
            self.connection.rollback()


