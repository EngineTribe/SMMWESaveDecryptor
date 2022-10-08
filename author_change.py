import base64
import rapidjson

from decoder import SMMWE_KEY, sha1_string_utf8_hmac

filename = 'JohnHK.swe'
new_author_name = 'YidaozhanYa'
json = rapidjson.loads(base64.b64decode(open(filename, 'r').read()[:-40].encode()).decode())
original_author_name = json['MAIN']['AJUSTES'][0]['user']
json['MAIN']['AJUSTES'][0]['user'] = new_author_name
level_encoded_string = base64.b64encode(rapidjson.dumps(json).encode()).decode()
level_signed_string = level_encoded_string + sha1_string_utf8_hmac(SMMWE_KEY, level_encoded_string)
open(filename.replace('.swe', '_modified.swe'), 'w').write(level_signed_string)
print('Author name was changed from ' + original_author_name + ' to ' + new_author_name)
