from scripts.dao.analytics_dao import *
from scripts.services.json_service import *
from scripts.services.xml_service import *
from scripts.utils.console_utils import *

analyticsDB = AnalyticsDB("root", "root", "127.0.0.1")
xml_service = XMLService("D:\Projects\Python\YandexAnalytics\history_data\data_download.xml")


# СОБЫТИЯ
json_service = JSONService("D:\Projects\Python\YandexAnalytics\yandex metrica\events.json")
i = 0
"""Получаем дату с последним скачиванем"""
data_download_events = xml_service.get_dict_data()["data_download_events"]
"""Берем все события не раньше последнего скачивания"""
events_later_data = json_service.get_dict_data_later_date(data_download_events, "event_datetime")

"""Добавляем все в базу"""
if len(events_later_data) != 0:
    printProgressBar(0, len(events_later_data), prefix='Progress add errors events:', suffix='Complete', length=50)
    for event in events_later_data:
        analyticsDB.insert_events(event)
        printProgressBar(i, len(events_later_data), prefix='Progress add events:', suffix='Complete', length=50)
        i = i + 1

    """ Получаем последнию дату в событиях"""
    last_date_event = json_service.get_max_data("event_datetime")
    """ Записываем последнию дату в конфиг"""
    xml_service.set_data("data_download_events", last_date_event)
print("\n")

# ОШИБКИ
json_service = JSONService("D:\Projects\Python\YandexAnalytics\yandex metrica\errors.json")
i = 0
"""Получаем дату с последним скачиванем"""
data_download_errors = xml_service.get_dict_data()["data_download_errors"]
"""Берем все события не раньше последнего скачивания"""
error_later_data = json_service.get_dict_data_later_date(data_download_errors, "error_datetime")

"""Добавляем все в базу"""
if len(error_later_data) != 0:
    printProgressBar(0, len(error_later_data), prefix='Progress add errors:', suffix='Complete', length=50)
    for error in error_later_data:
        analyticsDB.insert_error(error)
        printProgressBar(i, len(error_later_data), prefix='Progress add errors:', suffix='Complete', length=50)
        i = i + 1

    """ Получаем последнию дату в событиях"""
    last_date_error = json_service.get_max_data("error_datetime")
    """ Записываем последнию дату в конфиг"""
    xml_service.set_data("data_download_errors", last_date_error)
print("\n")


# УСТАНОВКИ
json_service = JSONService("D:\Projects\Python\YandexAnalytics\yandex metrica\installations.json")
i = 0
"""Получаем дату с последним скачиванем"""
data_download_installations = xml_service.get_dict_data()["data_download_installs"]
"""Берем все события не раньше последнего скачивания"""
install_later_data = json_service.get_dict_data_later_date(data_download_installations, "install_datetime")

"""Добавляем все в базу"""
if len(install_later_data) != 0:
    printProgressBar(0, len(install_later_data), prefix='Progress add installs:', suffix='Complete', length=50)
    for install in install_later_data:
        analyticsDB.insert_installation(install)
        printProgressBar(i, len(install_later_data), prefix='Progress add installs:', suffix='Complete', length=50)
        i = i + 1

    """ Получаем последнию дату в событиях"""
    last_date_install = json_service.get_max_data("install_datetime")
    """ Записываем последнию дату в конфиг"""
    xml_service.set_data("data_download_installs", last_date_install)
print("\n")