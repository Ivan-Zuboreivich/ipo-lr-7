print("start code …")
import json

with open("dump.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

# Получаем номер квалификации
qualification_number = input("Введите номер квалификации: ").strip()

# Ищем квалификацию
qualification_data = None

for item in data:
    # Проверяем, что это объект квалификации
    if item.get('model') == 'data.skill':
        fields = item.get('fields', {})

        # Проверяем номер квалификации в разных полях
        if (fields.get('code') == qualification_number or
                fields.get('full_code') == qualification_number):
            qualification_data = fields
            break

# Выводим результат
if not qualification_data:
    print("=============== Не найдено ===============")
else:
    print("=============== Найдено ===============")

    # Основная специальность (если введен основной код)
    if len(qualification_number) <= 13:  # Основной код типа "4-02-0413-01"
        specialty = qualification_data.get('title', '')
        education_level = qualification_data.get('education_level', '')
        code = qualification_data.get('code', '')
        print({code}, '>> Специальность ', {specialty}, {education_level})

    # Конкретная квалификация (если введен полный код)
    if len(qualification_number) > 13:  # Полный код типа "4-02-0413-01-02"
        name = qualification_data.get('title', '')
        full_code = qualification_data.get('code', '')
        print({full_code}, ">> Квалификация ", {name})
print("end code …")
