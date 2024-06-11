'''
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

header
payload
signature

'''

from jose import jwt

# dane, które będą zawarte w tokenie
payload = {"sub": "1234567890", "name": "John Doe"}

# tworzenie tokena z kluczem symetrycznym
encoded = jwt.encode(payload, "secret_key", algorithm='HS256')
print(encoded)

# weryfikacja tokena
decoded = jwt.decode(encoded, "secret_key", algorithms=['HS256'])
print(decoded)
