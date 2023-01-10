#!/usr/bin/env python

import json
from smmwe import dict_to_level_string

json_name: str = "test.json"
json_handle = open(json_name, 'r')

output_swe_name: str = json_name.replace('.json', '.swe')
output_swe_handle = open(output_swe_name, 'w')

output_swe_handle.write(
    dict_to_level_string(
        json.loads(
            json_handle.read()
            )
        )
    )
