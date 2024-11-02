class TaskManager:
    def __init__(self):
        self.data_s = {}

    def new_task(self,val,kek):
        task = {kek:val}
        key_d = int(str(task.keys())[-3])
        if key_d in self.data_s:
            self.data_s[key_d].append(val)  # просто добавляем задачу в список
        else:
            self.data_s[key_d] = [val]  # если приоритета нет, создаём список с задачей


    def __str__(self):
        formated_data = ''
        sorted_dict = sorted(self.data_s.items())
        for key, valye in sorted_dict:
            formated_data += f'{key} - {'; '.join(valye)} \n'
        return formated_data



manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)


