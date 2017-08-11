""" Class is an event model"""


# ---------------------------------------------------------------------
# Program by Pinchukov Artur
#
# Version     Data      Info
#  1.0     11.08.2017
# ---------------------------------------------------------------------

class Event:

    """ The method init class"""
    def __init__(self, android_id, app_package_name, app_version_name, appmetrica_device_id, city, connection_type,
                 country_iso_code, device_locale, device_manufacturer, device_model, device_type, event_datetime,
                 event_json, event_name, event_receive_datetime, event_receive_timestamp, event_timestamp, google_aid,
                 ios_ifa, ios_ifv, mcc, mnc, operator_name, os_name, os_version):
        self.android_id = android_id
        self.app_package_name = app_package_name
        self.app_version_name = app_version_name
        self.appmetrica_device_id = appmetrica_device_id
        self.city = city
        self.connection_type = connection_type
        self.country_iso_code = country_iso_code
        self.device_locale = device_locale
        self.device_manufacturer = device_manufacturer
        self.device_model = device_model
        self.device_type = device_type
        self.event_datetime = event_datetime
        self.event_json = event_json
        self.event_name = event_name
        self.event_receive_datetime = event_receive_datetime
        self.event_receive_timestamp = event_receive_timestamp
        self.event_timestamp = event_timestamp
        self.google_aid = google_aid
        self.ios_ifa = ios_ifa
        self.ios_ifv = ios_ifv
        self.mcc = mcc
        self.mnc = mnc
        self.operator_name = operator_name
        self.os_name = os_name
        self.os_version = os_version