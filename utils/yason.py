#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Time    : 2017/9/21 17:15
# @Author  : Bob
# @Website : www.nagexiucai.com
# @E-Mail  : me@nagexiucai.com
# @Summary : Yet Another Script Object Notation。

import yaml
import json
import cStringIO
from datetime import datetime, date, time

FILEPATH = "./yason"

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, time):
            return obj.strftime('%H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

with open(FILEPATH+".yaml") as syaml:
    oyaml = yaml.load(syaml)
    mockyaml = cStringIO.StringIO()
    json.dump(oyaml, mockyaml, cls=CJsonEncoder)
    print mockyaml.getvalue()
    mockyaml.close()

class CYamlDumper(yaml.Dumper):
    def represent_unicode(self, data):
        return self.represent_scalar("$", data)

CYamlDumper.add_representer(unicode, CYamlDumper.represent_unicode)

with open(FILEPATH+".json") as sjson:
    ojson = json.load(sjson)
    mockjson = cStringIO.StringIO()
    yaml.dump(ojson, mockjson, Dumper=CYamlDumper)
    draft = mockjson.getvalue()
    print(draft.replace("!<$> ", "").replace("'", ""))
    mockjson.close()
