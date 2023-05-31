### Нагрузочные тесты приложения Petstore
**Перед запуском тестов установить зависимости проекта используя команду:**
- `pip install -r requirements.txt`

**Запуск всех тестов производится командой:**
- `locust -f main.py --host=https://petstore.swagger.io/v2`

Примечаение: чтобы поднять locust на другом порту, необходимо добавить флаг -Р: 
- `locust -f main.py --host=https://petstore.swagger.io/v2 -P 1234`

[API Docs](https://petstore.swagger.io/)