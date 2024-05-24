import hmac
import base64
import struct
import hashlib as hash
import time

def hmac_based_otp(interval, secret_key):
    key = base64.b32decode(secret_key, True)
    msg = struct.pack(">Q", interval)
    h = hmac.new(key, msg, hash.sha1).digest()
    o = o = h[19] & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

def totp(secret_key):
    otp =hmac_based_otp(int(time.time())//30, secret_key)
    otp = str(otp)
    while len(otp)<6:
        otp+='0'
    return otp