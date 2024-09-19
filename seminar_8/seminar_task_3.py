import json
import csv
with open("file.json","r",encoding="utf-8") as f_json, \
     open("table.csv","w",newline = "") as f_csv:
    data = json.load(f_json)
    write_csv = csv.writer(f_csv)
    write_csv.writerow(['lvl','name','ID'])
    for key in data:
        for item in data[key]:
            write_csv.writerow([key,item["name"],item['id']])


