import json
import mysql.connector

def load_secrets():
    with open('secrets.json') as json_file:
        data = json.load(json_file)
        # print(data['host'], data['port'], data['user'], data['password'])
        host, port, user, password = data['host'], int(data['port']), data['user'], data['password']
    return host, port, user, password

def connect_mysql(host, port, user, password):
    print(host, port, user, password)
    mydb = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password
    )
    print(mydb)

if __name__ == '__main__':
    host, port, user, password = load_secrets()
    connect_mysql(host, port, user, password)
