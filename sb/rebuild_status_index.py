import requests

import json
import time

headers = {'Content-Type': 'application/json', "User-Agent": "Snowball Android 1.5"}


def run(file_name):
    fw = open(file_name + "_res", "w")
    i = 1
    for line in open(file_name, "r"):
        data = line.strip().split("\t")
        sid = data[0]
        rebuild_status_index(sid)
        if i % 1000 == 0:
            time.sleep(1)
            print("sleep" + i)
        i += 1

    fw.close()


def rebuild_status_index(sid):
    try:
        url = "http://10.10.212.83:8080/internal/search/admin/status/create_index.json?index=status_v7&status_id=" + sid
        response = requests.get(url, headers=headers)
        return json.loads(response.text)
    except Exception as err:
        print("insert", sid, err)


# print(get_status_create_time("195002557")["createdAt"])
run("/Users/dongyf/Desktop/ids.csv")

# rebuild_status_index("201938294")
