from typing import Dict

from src.common.generate_auth_token import generate_auth_token

TEST_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDIzi1aV7xG1BGjwf1ZsCxiMO5jdYEPVfdPDLbBQtMD4VZlNb4p
s2B6bExyLisOUxnlhEqdVn424EHIFRwNAV3eo0GcRrEGT4u57+Esqy9QQmvknJaA
+oBFlzCpMLV3clQIm6ropbVtgqQtnLH19WJMfal3nwB/v8Nle2XNQ7DJKwIDAQAB
AoGAHNj5zPvDsY0vx43L3sGfbq/G34T2+IQKFlImQxddhzYtGjchTY5Wct/yD4kw
aEtp8f4SVg4h7bJD4QGfWQL0QBGdk84Q5y29vau3XxHMmZn6URHqMs6RciQDzKdB
De/zb1rn3vOQuZIXO+ODhbK4cWPm/u4QyObzSAX2sYigyzkCQQDnaTqyNuE8LLxN
QVxJIaRARr4Y8UvxtS+sVhK4NqeIgw9x+TsDoMeePZuZZ6HW9azzSlGERnMuQnil
GgypQUUXAkEA3iRsB+jN25P5YY5PHTA/XbLCEM/ZhFc78dD4p5j24J2hB1ibBdoa
U9xHfXlV4S/nSYnlqS+0NLlfqBRZ+hxRDQJBAJyL/HA5Xg+mN9CPic3TW1k8Qjd/
bR/bsZ+FLu690oIwH0+8Cec/aisrhEq3560Sz+hZ+2Ffg2XlA9a1E6GgjQsCQQCa
cvxhq22lo4aaW5WKF8eW3/iqM7lqmDRndwHLlUDg/ve84dA3C2OOtvNFvB0HyoSm
zqfNMAu9NL3bYPsGOLXpAkABkLj2TbaFGbMVceGAeVbTR0OrU8DC4x+HcQMBYwsy
BT/C0/PFVtrscU8wbMsXizjYfz5MVyeglVB0ToZeQ8mZ
-----END RSA PRIVATE KEY-----
"""

TEST_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDIzi1aV7xG1BGjwf1ZsCxiMO5j
dYEPVfdPDLbBQtMD4VZlNb4ps2B6bExyLisOUxnlhEqdVn424EHIFRwNAV3eo0Gc
RrEGT4u57+Esqy9QQmvknJaA+oBFlzCpMLV3clQIm6ropbVtgqQtnLH19WJMfal3
nwB/v8Nle2XNQ7DJKwIDAQAB
-----END PUBLIC KEY-----
"""


def sign_jwt(user_id: str, expires: int = 180) -> Dict[str, str]:
    token = generate_auth_token(expires_in=expires, id=user_id)
    return token


NO_TOKEN = ""
BAD_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJlbWFpbCI6InBldGEtaG9sZGluZ0B5YW5kZXgucnUiLCJleHAiOjE2Nzc3NTEz"
EXP_TOKEN = sign_jwt(user_id=str(637925), expires=1)
