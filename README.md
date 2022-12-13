# Умный дом

1. Создать датчик. Указываются название и описание датчика.
```commandline
POST http://localhost:8000/api/create/?name=Новый+датчик+3&discription=Новый+датчик
name - Имя датчика
discription - Описание датчика
```
2. Изменить датчик. Указываются название и/или описание.
```commandline
PATCH http://localhost:8000/api/patch/?id=3&name=New+name&discription=New+discription
id - Номер изменяемого датчика
name - Новое имя
discription - Новое описание
```
3. Добавить измерение. Указываются ID датчика и температура.
```commandline
POST http://localhost:8000/api/addtemp/?id=4&temp=80
id - Номер датчика, в который вносим измерение
temp - Заносимое значение температуры (int, float)
```
4. Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание.
```commandline
GET http://localhost:8000/api/list/
output - json file
```


## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Вам необходимо будет создать базу в postgres и прогнать миграции:

```base
python manage.py migrate
```

Выполнить команду:

```bash
python manage.py runserver
```
