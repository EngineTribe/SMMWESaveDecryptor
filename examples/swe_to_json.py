#!/usr/bin/env python

import json
from smmwe import level_string_to_dict

swe_name: str = "test.swe"
swe_handle = open(swe_name, 'r')

output_json_name: str = swe_name.replace('.swe', '.json')
output_json_handle = open(output_json_name, 'w')

output_json_handle.write(
    json.dumps(
        level_string_to_dict(
            swe_handle.read()
            )
        )
    )
