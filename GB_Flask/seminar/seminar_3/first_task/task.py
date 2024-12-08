students_data = {
    # Направление "Him Bio"
    'Him Bio': [
        {'username': 'Alexei', 'surename': 'Ivanov', 'sex': 'man'},
        {'username': 'Irina', 'surename': 'Petrova', 'sex': 'woman'},
        {'username': 'Mikhail', 'surename': 'Sidorov', 'sex': 'man'},
        {'username': 'Elena', 'surename': 'Kuznetsova', 'sex': 'woman'},
        {'username': 'Dmitry', 'surename': 'Fedorov', 'sex': 'man'},
        {'username': 'Natalia', 'surename': 'Morozova', 'sex': 'woman'},
        {'username': 'Pavel', 'surename': 'Semenov', 'sex': 'man'}
    ],

    # Направление "Soc Economy"
    'Soc Economy': [
        {'username': 'Vladimir', 'surename': 'Smirnov', 'sex': 'man'},
        {'username': 'Maria', 'surename': 'Alexandrova', 'sex': 'woman'},
        {'username': 'Oleg', 'surename': 'Novikov', 'sex': 'man'},
        {'username': 'Svetlana', 'surename': 'Vasilieva', 'sex': 'woman'},
        {'username': 'Andrei', 'surename': 'Karpov', 'sex': 'man'},
        {'username': 'Tatiana', 'surename': 'Orlova', 'sex': 'woman'},
        {'username': 'Roman', 'surename': 'Kozlov', 'sex': 'man'}
    ],

    # Направление "Fitz Math"
    'Fitz Math': [
        {'username': 'Ivan', 'surename': 'Gavrilov', 'sex': 'man'},
        {'username': 'Anna', 'surename': 'Nikolaeva', 'sex': 'woman'},
        {'username': 'Konstantin', 'surename': 'Belyaev', 'sex': 'man'},
        {'username': 'Olga', 'surename': 'Klimova', 'sex': 'woman'},
        {'username': 'Maxim', 'surename': 'Zaitsev', 'sex': 'man'},
        {'username': 'Yulia', 'surename': 'Baranova', 'sex': 'woman'},
        {'username': 'Alexandra', 'surename': 'Yarovaya', 'sex': 'woman'}
    ]
}

for i, sc_dir in enumerate(students_data, start=1):
    for people in students_data[sc_dir]:
        # print(i)
        print(len(students_data[sc_dir]))
        # # id = students_data[sc_dir]
        # #
        # # print(id)
        # print(id)
        # user_name=people['username']
        # surename=people['surename']
        # sex=people['sex']
        # group = sc_dir
        # print(sc_dir)

