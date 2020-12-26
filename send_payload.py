import json
import csv


def load_schema(path):
    with open(path) as json_file:
        data = json.load(json_file)
        for p in data:
            print(p)


def stream_csv_file(path, delimiter):
    with open(path, "r") as csv_data_source:
        rows = csv.reader(csv_data_source, delimiter=delimiter)
        for i, row in enumerate(rows):
            print('[{}] : {}'.format(i, row))


def send_payload(values):
    print(values)


if __name__ == '__main__':
    load_schema('configs/schema/iris_schema.json')
    stream_csv_file('csv_data_source/Iris.csv', ",")
