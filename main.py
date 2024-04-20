import json

# Json - текстовый формат обмена данными, основанный на языке JavaScript 
# Поддерживаемые типы данных:
# ключ - Строка
# значение - Строка, целое/вещественное число, 
#            логическое значение, список, json-объект
user = {
    "name": "Semyon",
    "age": 24,
    "is_teacher": True,
    "skills": ["C#", "Python"],
    "address": {
            "city": "Tomsk",
            "street": "Gercena",
            "house": 18
    },
    "phones": ["8-913-823-82-62", "8-995-433-82-62"]  
}

# Сериализация - процесс перевода программных структур данных в формат для хранения
# json.dumps() - принимает программную структуру, возвращает json-строку
# indent - добавляет отступы при преобразовании программной структуры в json-формат
# user_json = json.dumps(user)
user_json = json.dumps(user, indent=2)
print(user_json)

# По умолчанию символы кирилицы заменяются на кодировку стандартную для json-формата,
# параметр ensure_ascii экранирует, не ASCII символы, то есть подставляет код символа,
# а не сам символ, мы это экранирование отключаем 
user_rus = {
    "name": "Семён",
    "city": "Томск"
}
# user_rus_json = json.dumps(user_rus, indent=2)
user_rus_json = json.dumps(user_rus, indent=2, ensure_ascii=False)
print(user_rus_json)

# json.dump() - принимает программную структуру, возвращает json-файл
file = open('user.json', 'w')
json.dump(user, file, indent=2)

file = open('user_rus.json', 'w', encoding='utf-8')
json.dump(user_rus, file, indent=2, ensure_ascii=False)

# Десериализация - процесс перевода хранимых данных в программную структуру
# json.loads() - преобразует json-строку в программную структуру
print(json.loads(user_json)) # На выходе мы получим не json, а привычный нам словарь

# json.load() - преобразует json-файл в программную структуру
file = open('user.json', encoding='utf-8') 
user_data = json.load(file) #  На выходе мы получим не json, а привычный нам словарь
print(user_data['name']) # Выводи значение ключа 'name'
