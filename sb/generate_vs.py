def run(file_read, file_write, prefix1, prefix2):
    fw = open(file_write, "w")
    for line in open(file_read, "r"):
        fw.write(prefix1 + line.strip() + "\t" + prefix2 + line.strip() + "\n")
    fw.close()


run("/Users/dongyf/dongyf/data/vs/hot_stock_name",
    "/Users/dongyf/dongyf/data/vs/knowing_query_vs_search_query",
    "http://rc.search.query.snowballfinance.com/query/internal/knowing_query/status?uid=2057129123&query=",
    "http://rc.search.query.snowballfinance.com/query/internal/no_knowing_query/status?u=2057129123&sortId=1&count=10&page=1&q=")
