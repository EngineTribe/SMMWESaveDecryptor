from hashlib import sha1
import hmac

SMMWE_KEY = "2559F35097-2021"


def sha1_string_utf8_hmac(key: str, string: str):
    hashed = hmac.new(key.encode('utf-8'), string.encode('utf-8'), sha1)
    return hashed.hexdigest()
