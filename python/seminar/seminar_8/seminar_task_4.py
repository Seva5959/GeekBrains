import csv
import json

def change_csv(original_name,new_name):
    with open(original_name,"r",newline="") as f_old, \
        open(new_name,"w",newline="") as f_new:
        read = csv.reader(f_old)
        write = csv.writer(f_new)
        headers = next(read)
        write.writerow(headers)

        for row in read:
            name, lvl, id = row
            id = id.zfill(10)
            name = name.strip().title()
            write.writerow([name, lvl, id])

def save_json():
    data = []
    with  open("table_4.csv","r",newline="") as f_csv:
        csv_open = csv.reader(f_csv)

        for row in csv_open:
            name , lvl , id = row
            data.append({
                "name": name,
                "lvl": lvl,
                "id": id
            })
        with open("json_task_4.json","w", encoding="utf-8")as f_json:
            json.dump(data,f_json,indent=4)

change_csv("table.csv", "table_4.csv")
save_json()