import json
import csv


def load_schema(schema_path):
    with open(schema_path) as json_file:
        data = json.load(json_file)
        for p in data:
            print(p)

def stream_csv_file(csv_path, delimiter):
    with open(csv_path, "r") as csv_data_source:
        rows = csv.reader(csv_data_source, delimiter=delimiter)
        for i, row in enumerate(rows):
            print('[{}] : {}'.format(i, row))
            send_payload(row)


def send_payload(values):
    print(values)


def silo_check(job_conf_path):
    with open(job_conf_path) as json_file:
        data = json.load(json_file)
        print(data)


if __name__ == '__main__':
    load_schema('configs/schema/iris_schema.json')
    stream_csv_file('csv_data_source/Iris.csv', ",")
    silo_check('configs/job.json')
