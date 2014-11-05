from pprint import pprint

test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]


##CREATE TWO NEW LISTS ONE FOR EACH
# STOCK TICKER SYMBOL e.g. APPL and MSFT

stocks = {}

for item in test_data:
    if item[1] not in stocks:
        stocks[item[1]] = [item]
        del item[1]
    else:
        stocks[item[1]].append(item)
        del item[1]

pprint(stocks)





