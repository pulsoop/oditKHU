import jwt
import datetime

def generateAccessToken(user):
    exp = datetime.datetime.now() + datetime.timedelta(hours=1)

    payload = {
        'exp': round(exp.timestamp(), 0),
        'id': user['id'],
        'u_id': user['u_id'],
        'name': user['name'],
        'email': user['email'],
        'phone': user['phone']
    }
    encoded = jwt.encode(payload, 'dbdbdp', algorithm='HS256')
    return encoded.decode('utf-8')

