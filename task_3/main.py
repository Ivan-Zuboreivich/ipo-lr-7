import json
#Зуборевич, вариант 2
print("start code...")


# Главный цикл программы
while True:
    print("\n" + "=============================================================")
    print("МЕНЮ:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")
    print("============================================================")

    choice = input("Сделайте свой выбор: ").strip()

    # 1. Вывести все записи
    if choice == "1":
        with open("data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)

        print("\n" + "===========================================================")
        print("ВСЕ ЗАПИСИ:")
        print("===========================================================")

        if not data:
            print("Записей нет")
        else:
            for i, record in enumerate(data, 1):
                print("Запись #", {i}, ":")
                for key, value in record.items():
                    print({key}, ":", {value})
                print("-" * 30)

    # 2. Вывести запись по полю
    elif choice == "2":
        record_id = input("Введите ID записи для поиска: ").strip()

        with open("data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)

        found = False
        for i, record in enumerate(data):
            if record.get('id') == record_id:
                print("\n" + "Найдена запись на позиции", {i + 1})
                print("==============================")
                for key, value in record.items():
                    print({key}, ":", {value})
                found = True
                break

        if not found:
            print("\n" + 'Запись с ID ', {record_id}, ' не найдена!')

    # 3. Добавить запись
    elif choice == "3":
        print("\n" + "Добавление новой записи:")
        new_record = {}

        new_record['id'] = input("Введите ID: ").strip()
        new_record['name'] = input("Введите имя: ").strip()
        new_record['latin_name'] = input("Введите научное название: ").strip()
        iw = input("Является ли цветок краснокнижным?")
        print("1.Да")
        print("2.Нет")
        if (iw == 1):
            new_record['is_red_book_flower'] = "Да"
        else:
            new_record['is_red_book_flower'] = "Нет"
        new_record['price'] = input("Введите цену: ").strip()
        with open("data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)

        data.append(new_record)

        with open("data.json", 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print("Запись успешно добавлена!")

    # 4. Удалить запись по полю
    elif choice == "4":
        record_id = input("Введите ID записи для удаления: ").strip()

        with open("data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)

        found = False
        new_data = []
        for record in data:
            if record.get('id') == record_id:
                found = True
                print("Удалена запись:")
            else:
                new_data.append(record)

        if found:
            with open("data.json", 'w', encoding='utf-8') as file:
                json.dump(new_data, file, ensure_ascii=False, indent=2)
            print("Запись успешно удалена!")
        else:
            print("\nЗапись с ID ", {record_id}, "не найдена!")

    # 5. Выйти из программы
    elif choice == "5":
        print("\n" + "Программа завершена.")
        break

    # Неверный выбор
    else:
        print("Неверный выбор! Пожалуйста, выберите пункт от 1 до 5.")
print("end code...")
