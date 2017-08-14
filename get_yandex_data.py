from requests import *  # install lib


request_str = "https://appmetrica.yandex.ru/export-log?url=%2Flogs-exporter%2Fevents%2Fjson%2F%3Fapplication_id" \
              "%3D176450%26date_since%3D2017-08-08%252000%253A00%253A00%26date_until%3D2017-08-14%252023%253A59" \
              "%253A59%26date_dimension%3Dreceive%26use_utf8_bom%3Dtrue%26fields%3Dios_ifa%252Cios_ifv%252Cgoogle_aid" \
              "%252Candroid_id%252Cos_name%252Cos_version%252Cdevice_manufacturer%252Cdevice_model%252Cdevice_type" \
              "%252Cdevice_locale%252Capp_version_name%252Capp_package_name%252Cevent_name%252Cevent_json" \
              "%252Cevent_datetime%252Cevent_timestamp%252Cevent_receive_datetime%252Cevent_receive_timestamp" \
              "%252Cconnection_type%252Coperator_name%252Cmcc%252Cmnc%252Ccountry_iso_code%252Ccity" \
              "%252Cappmetrica_device_id%26inteface%3D1?oauth_token=05dd3dd84ff948fdae2bc4fb91f13e22bb1f289ceef0037"

get_request = get(request_str, headers={"Authorization": "OAuth 05dd3dd84ff948fdae2bc4fb91f13e22bb1f289ceef0037"})
print(get_request.status_code)
print(get_request.text)
