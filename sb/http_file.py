import requests
import time

i = 0
# for line in open("/Users/dongyf/dongyf/data/test/search_rank_sled", "r"):
for line in open("/Users/dongyf/dongyf/data/test/search_kowing_query_load", "r"):
    try:
        response = requests.get(line.strip())
        i += 1
        if i % 100 == 0:
            time.sleep(1)
            print(i)
    except Exception as err:
        print("insert", line, err)
