from requests import *  # install lib
import time
import datetime
import os
from analytics_сontroller import AnalyticsController
from scripts.dao.analytics_dao import AnalyticsDB

# СТАТИЧЕСКИЕ ДАННЫЕ
TOKEN = "AQAAAAATpP0XAAR70vxUpgjrAkq_h3IGIcgKL-0"
TIME_SLEEP = 2  # время между запросвми в яндекс для проверки о готовности пакета
COUNT_PACK = 100  # количесвто пакетов, на которые разбиваются данные
# ДАННЫЕ
# текущая дата
today = datetime.datetime.today()
# папка для хранения файлов
tmp_folder_path = os.path.abspath(__file__).replace("get_yandex_installations.py", "tmp\\")
# класс для работы с БД (лежит в папках scripts/dao)
analytics_db = AnalyticsDB("root", "root", "127.0.0.1")
# максимальные даты в таблицах, берется из БД
last_download_events = datetime.datetime.strptime(analytics_db.get_max_event_datetime(), '%Y-%m-%d %H:%M:%S')
last_download_errors = datetime.datetime.strptime(analytics_db.get_max_errors_datetime(), '%Y-%m-%d %H:%M:%S')
last_download_installations = datetime.datetime.strptime(analytics_db.get_max_installation_datetime(), '%Y-%m-%d %H:%M:%S')
last_download_crashes = datetime.datetime.strptime(analytics_db.get_max_crashes_datetime(), '%Y-%m-%d %H:%M:%S')
# контролер для парсинга json файлов и отправка их в бд, методы приниают лист с путями до json файлов
analytics_controller = AnalyticsController(analytics_db)


# метод добавлет нолик в начало даты, если она меньше 10 т к яндекс не кушает дату с одним значением
def check_data(value):
    if int(value) < 10:
        return "0" + str(value)
    else:
        return str(value)


DATA_START_EVENT = str(last_download_events.date()) + "%20" + check_data(last_download_events.hour) + "%3A" + check_data(last_download_events.minute) + "%3A" + check_data(last_download_events.second)
DATA_START_ERROR = str(last_download_errors.date()) + "%20" + check_data(last_download_errors.hour) + "%3A" + check_data(last_download_errors.minute) + "%3A" + check_data(last_download_errors.second)
DATA_START_INSTALLATIONS = str(last_download_installations.date()) + "%20" + check_data(last_download_installations.hour) + "%3A" + check_data(last_download_installations.minute) + "%3A" + check_data(last_download_installations.second)
DATA_START_CRASHES = str(last_download_crashes.date()) + "%20" + check_data(last_download_crashes.hour) + "%3A" + check_data(last_download_crashes.minute) + "%3A" + check_data(last_download_crashes.second)
DATA_END = str(today.date()) + "%20" + check_data(today.hour) + "%3A" + check_data(today.minute) + "%3A" + check_data(today.second)

print("дата начала промежутка времени событий - "+str(last_download_events))
print("дата начала промежутка времени ошибок - "+str(last_download_errors))
print("дата начала промежутка времени установок - "+str(last_download_installations))
print("дата конца промежутка времени(общее)- "+str(today))



"""
#
#
# РАБОТА С УСТАНОВКАМИ
#
#
"""
list_installations = list()
for i in range(COUNT_PACK):
    print("номер части пакета - " + str(i+1))
    # ЗАПРОС В ЯНДЕКС
    request_str = "https://api.appmetrica.yandex.ru/logs/v1/export/installations.json?application_id=176450" \
                  "" \
                  "&date_since=" + DATA_START_INSTALLATIONS + "&date_until=" + DATA_END + \
                  "" \
                  "&date_dimension=default&use_utf8_bom=true&fields=publisher_name%2Cpublisher_id%2Ctracker_name%2" \
                  "Ctracking_id%2Cclick_timestamp%2Cclick_datetime%2Cclick_ipv6%2Cclick_url_parameters%2Cclick_id%2" \
                  "Cclick_user_agent%2Cinstall_datetime%2Cmatch_type%2Cinstall_timestamp%2Cinstall_receive_datetime%" \
                  "2Cinstall_receive_timestamp%2Cinstall_ipv6%2Cis_reinstallation%2Cios_ifa%2Cios_ifv%2Candroid_id%" \
                  "2Cgoogle_aid%2Cos_name%2Cos_version%2Cdevice_manufacturer%2Cdevice_model%2Cdevice_locale%2Cdevice_" \
                  "type%2Capp_version_name%2Capp_package_name%2Cconnection_type%2Coperator_name%2Cmcc%2Cmnc%2Ccountry_" \
                  "iso_code%2Ccity%2Cappmetrica_device_id" \
                  + "&parts_count=" + str(COUNT_PACK) +"&part_number=" + str(i) + "&oauth_token=" + TOKEN

    # выполняем запрос пока не получим хороший ответ
    while True:
        get_request = get(request_str)
        if get_request.status_code == 200:
            print(get_request.status_code)
            break
        else:
            print(get_request.status_code)
            print(get_request.text)
        time.sleep(TIME_SLEEP)
    # сохраняем в файл
    f = open(tmp_folder_path+"installations-" + str(i) + ".json", "wb")
    f.write(get_request.text.encode(encoding='utf_8_sig', errors='strict'))
    f.close()
    # добавляем путь до json файла в лист
    list_installations.append(tmp_folder_path+"installations-" + str(i) + ".json")
# отправляем лист контролеру для дальнейшего парсинга файлов и отправки в БД
analytics_controller.add_installations(list_installations)


"""
#
#
# РАБОТА С ОШИБКАМИ
#
#
"""
list_errors = list()
for i in range(COUNT_PACK):
    print("номер части пакета - " + str(i+1))
    # ЗАПРОС В ЯНДЕКС
    request_str = "https://api.appmetrica.yandex.ru/logs/v1/export/errors.json?application_id=176450" \
                  "" \
                  "&date_since=" + DATA_START_ERROR + "&date_until=" + DATA_END + \
                  "" \
                  "&date_dimension=default&use_utf8_bom=true&fields=ios_ifa%2Cios_ifv%2Candroid_id%2Cgoogle_aid%" \
                  "2Cwindows_aid%2Cos_name%2Cos_version%2Cdevice_manufacturer%2Cdevice_model%2Cdevice_type%2Cdevice_" \
                  "locale%2Capp_version_name%2Capp_package_name%2Cerror%2Cerror_id%2Cerror_datetime%2Cerror_timestam" \
                  "p%2Cerror_receive_datetime%2Cerror_receive_timestamp%2Cconnection_type%2Coperator_name%2Cmcc%2Cmnc%" \
                  "2Ccountry_iso_code%2Ccity%2Cappmetrica_device_id" \
                  + "&parts_count=" + str(COUNT_PACK) +"&part_number=" + str(i) + "&oauth_token=" + TOKEN

    # выполняем запрос пока не получим хороший ответ
    while True:
        get_request = get(request_str)
        if get_request.status_code == 200:
            print(get_request.status_code)
            break
        else:
            print(get_request.status_code)
            print(get_request.text)
        time.sleep(TIME_SLEEP)
    # сохраняем в файл
    f = open(tmp_folder_path+"errors-" + str(i) + ".json", "wb")
    f.write(get_request.text.encode(encoding='utf_8_sig', errors='strict'))
    f.close()
    # добавляем путь до json файла в лист
    list_errors.append(tmp_folder_path+"errors-" + str(i) + ".json")
# отправляем лист контролеру для дальнейшего парсинга файлов и отправки в БД
analytics_controller.add_errors(list_errors)


"""
#
#
# РАБОТА С КРЭШАМИ
#
#
"""
list_crashes = list()
for i in range(COUNT_PACK):
    print("номер части пакета - " + str(i+1))
    # ЗАПРОС В ЯНДЕКС
    request_str = "https://api.appmetrica.yandex.ru/logs/v1/export/crashes.json?application_id=176450" \
                  "" \
                  "&date_since=" + DATA_START_CRASHES + "&date_until=" + DATA_END + \
                  "" \
                  "&date_dimension=default&use_utf8_bom=true&fields=ios_ifa%2Cios_ifv%2Candroid_id%2Cgoogle_aid%2Cwind" \
                  "ows_aid%2Cos_name%2Cos_version%2Cdevice_manufacturer%2Cdevice_model%2Cdevice_type%2Cdevice_locale%" \
                  "2Capp_version_name%2Capp_package_name%2Ccrash%2Ccrash_id%2Ccrash_group_id%2Ccrash_datetime%2Ccrash_t" \
                  "imestamp%2Ccrash_receive_datetime%2Ccrash_receive_timestamp%2Cconnection_type%2Coperator_name%2Cmcc%" \
                  "2Cmnc%2Ccountry_iso_code%2Ccity%2Cappmetrica_device_id" \
                  + "&parts_count=" + str(COUNT_PACK) +"&part_number=" + str(i) + "&oauth_token=" + TOKEN

    # выполняем запрос пока не получим хороший ответ
    while True:
        get_request = get(request_str)
        if get_request.status_code == 200:
            print(get_request.status_code)
            break
        else:
            print(get_request.status_code)
            print(get_request.text)
        time.sleep(TIME_SLEEP)
    # сохраняем в файл
    f = open(tmp_folder_path+"crashes-" + str(i) + ".json", "wb")
    f.write(get_request.text.encode(encoding='utf_8_sig', errors='strict'))
    f.close()
    # добавляем путь до json файла в лист
    list_crashes.append(tmp_folder_path+"crashes-" + str(i) + ".json")
# отправляем лист контролеру для дальнейшего парсинга файлов и отправки в БД
analytics_controller.add_crashes(list_crashes)