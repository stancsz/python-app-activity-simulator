import json


def load_secrets():
    with open('secrets.json') as json_file:
        data = json.load(json_file)
        print(data['host'], data['port'], data['user'], data['password'])
        host, port, user, password = data['host'], data['port'], data['user'], data['password']

if __name__ == '__main__':
    load_secrets()
