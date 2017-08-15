from requests import *  # install lib
import time
import urllib.request
import datetime
from scripts.services.xml_service import *


# СТАТИЧЕСКИЕ ДАННЫЕ
TOKEN = "AQAAAAATpP0XAAR70vxUpgjrAkq_h3IGIcgKL-0"
# ДАННЫЕ
today = datetime.datetime.today()
last_download_dict = XMLService("D:\Projects\Python\YandexAnalytics\history_data\data_download.xml").get_dict_data()
last_download = datetime.datetime.strptime(last_download_dict["data_download_events"], '%Y-%m-%d %H:%M:%S')


# метод добавлет нолик в начало даты, если она меньше 10 т к яндекс не кушает дату с одним значением
def check_data(value):
    if int(value) < 10:
        return "0" + str(value)
    else:
        return str(value)


DATA_START = str(last_download.date()) + "%20" + check_data(last_download.hour) + "%3A" + check_data(last_download.minute) + "%3A" + check_data(last_download.second)
DATA_END = str(today.date()) + "%20" + check_data(today.hour) + "%3A" + check_data(today.minute) + "%3A" + check_data(today.second)

print(DATA_START)
print(DATA_END)

# ЗАПРОС В ЯНДЕКС
request_str = "https://api.appmetrica.yandex.ru/logs/v1/export/events.json?application_id=176450" \
              "" \
              "&date_since=" + DATA_START + "&date_until=" + DATA_END + \
              "" \
              "&date_dimension=default&use_utf8_bom=true" \
              "&fields=ios_ifa%2Cios_ifv%2Candroid_id%2Cgoogle_aid%2Cos_name%2Cos_version%2Cdevice_manufacturer" \
              "%2Cdevice_model%2Cdevice_type%2Cdevice_locale%2Capp_version_name%2Capp_package_name%2Cevent_name" \
              "%2Cevent_json%2Cevent_datetime%2Cevent_timestamp%2Cevent_receive_datetime%2Cevent_receive_timestamp" \
              "%2Cconnection_type%2Coperator_name%2Cmcc%2Cmnc%2Ccountry_iso_code%2Ccity%2Cappmetrica_device_id" \
              "&oauth_token=" + TOKEN

print(request_str)

while True:
    get_request = get(request_str)
    if get_request.status_code == 202:
        print(get_request.status_code)
        print(get_request.text)
    else:
        print(get_request.status_code)
        break
    time.sleep(3)


#opener = urllib.request.build_opener()
#opener.addheaders = [('Encoding', 'gzip')]
#logo = opener.open(request_str).read()

f = open("events.json", "w") ##wb
f.write(get_request.text)
f.close()




