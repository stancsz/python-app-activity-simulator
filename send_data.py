import json
import csv
import mysql.connector
from mysql.connector import Error


def load_schema(schema_path):
    with open(schema_path) as json_file:
        data = json.load(json_file)
        for p in data:
            print(p)


def stream_csv_file(secret_path, job_conf_path, csv_path, delimiter):
    with open(secret_path) as json_file:
        secret = json.load(json_file)
    print(secret)

    with open(job_conf_path) as json_file:
        job = json.load(json_file)
    print(job)

    try:
        connection = mysql.connector.connect(host=secret['host'],
                                             database=job['iris']['database'],
                                             port=int(secret['port']),
                                             user=secret['user'],
                                             password=secret['password'])

        cursor = connection.cursor(prepared=True)

        sql_insert_query = "INSERT INTO " + job['iris']['table'] + " (Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species) VALUES (%s,%s,%s,%s,%s,%s)"
        with open(csv_path, "r") as csv_data_source:
            rows = csv.reader(csv_data_source, delimiter=delimiter)
            for i, row in enumerate(rows):
                # print('[{}] : {}'.format(i, row))
                send_payload(row)
                try:
                    insert_tuple_1 = (int(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4]),row[5])
                    cursor.execute(sql_insert_query, insert_tuple_1)
                except:
                    pass

        connection.commit()
        print("Data inserted successfully into employee table using the prepared statement")

    except mysql.connector.Error as error:
        print("parameterized query failed {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




def send_payload(values):
    print(values)



def silo_check(job_conf_path):
    with open(job_conf_path) as json_file:
        data = json.load(json_file)
        print(data)


if __name__ == '__main__':
    # load_schema('configs/schema/iris_schema.json')
    stream_csv_file('configs/secret.json', 'configs/job.json', 'csv_data_source/Iris.csv', ",")
    # silo_check('configs/job.json')
