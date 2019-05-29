import pymysql

db_info = {
    'host': 'db.dasom.io',
    'port': 3306,
    'user': 'root',
    'passwd': 'dasomDASOM',
    'db': 'dbdbdp',
    'charset': 'utf8'
}

def db_connect():
    try:
        return pymysql.connect(**db_info)
    except Exception as exc:
        raise Exception('MySQL Connection Failure : ' + str(exc))