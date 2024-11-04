def name(count):
    with open("data_task_2.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    if count > 4:
        return lines[count - 4].strip() if count - 4 < len(lines) else ""
    return lines[count].strip() if count < len(lines) else ""
def mix():
    results = []
    with open("data_task_1.txt", "r", encoding="utf-8") as f:
        for count, line in enumerate(f):
            line = line.strip()
            first, second = line.split("|")
            product = int(first) * float(second)
            if product < 0:
                name_result = name(count)
                results.append(f"{name_result}: {abs(product)}\n")

    with open("data_task_3.txt", "w", encoding="utf-8") as f:
        f.writelines(results)

mix()