from scripts.dao.analytics_dao import *
from scripts.services.json_service import *
from scripts.models.event import *

analyticsDB = AnalyticsDB("root", "root", "127.0.0.1")
json_service = JSONService("D:\Projects\Python\YandexAnalytics\yandex metrica\events.json")

# print(json_service.get_dict_data()["data"])
# print(len(json_service.get_dict_data()["data"]))
dict_data = json_service.get_dict_data()["data"]
i = 0
final_mass = ""
for event in dict_data:
    analyticsDB.insert_events(event)
    i = i + 1
    print(i)
