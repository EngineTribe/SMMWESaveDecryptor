from hashlib import sha1
import hmac
import json  # or rapidjson as json
from base64 import b64decode, b64encode

SMMWE_KEY = "2559F35097-2021"


def sha1_string_utf8_hmac(key: str, string: str) -> str:
    '''
    From https://github.com/JujuAdams/protect-your-savefiles
    Calculate SMM:WE save's hash section.
    '''
    hashed = hmac.new(key.encode('utf-8'), string.encode('utf-8'), sha1)
    return hashed.hexdigest()


def level_string_to_dict(level_string: str) -> dict:
    '''
    Load SMM:WE level's data section and return a dictionary.
    '''
    offset: int = 41 if level_string[-1] == '\x00' else 40
    return json.loads(b64decode(level_string[:-offset].encode()).decode())


def dict_to_level_string(level_dict: dict) -> str:
    '''
    Convert dictionary to SMM:WE level string with hash section.
    '''
    level_encoded_string = b64encode(json.dumps(level_dict).encode()).decode()
    return level_encoded_string + sha1_string_utf8_hmac(SMMWE_KEY, level_encoded_string)
