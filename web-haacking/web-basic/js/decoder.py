code = '01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001'

val =""
for i in code.split(' '):
    val +=chr(int(i,2))
print(val)


import base64
code = 'MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======'
print(base64.b32decode(code))

code = 'RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg=='
print(base64.b64decode(code).decode())


code = '68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f'
x=""
for i in code.split(' '):
    x += chr(int(i,16))
print(x)


code = "Ebgngr zr 13 cynprf!"
print(chr(13))
