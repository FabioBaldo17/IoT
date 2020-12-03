#!/usr/bin/env python

import datetime
import jwt

PROJECT_ID = 'master-iot-2020'
PRIVATE_KEY_FILE = 'esp_key_fabio_iot_private.pem'
ALGORITHM = 'ES256'

jeton = {
    'iat': datetime.datetime.utcnow(),
    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
    'aud': PROJECT_ID
}

with open(PRIVATE_KEY_FILE, 'r') as fichier:
    cle_privee = fichier.read()

print('JWT :')
print(jwt.encode(jeton, cle_privee, algorithm=ALGORITHM))
