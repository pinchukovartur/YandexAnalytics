import json

""" Class that provides methods for working with json"""


# ---------------------------------------------------------------------
# Program by Pinchukov Artur
#
# Version     Data      Info
#  1.0     11.08.2017
# ---------------------------------------------------------------------


class JSONService:
    """ The method init class"""
    def __init__(self, json_file):
        f = open(json_file, encoding="utf-8-sig")
        str_json = f.read().replace("\n", "")
        print(f.read())
        self.pars_str = json.loads(str_json, encoding="utf-8")

    """ The method init class"""
    def get_dict_data(self):
        return self.pars_str
