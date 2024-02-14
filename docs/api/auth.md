# API для авторизации

1. `<HOST>:<PORT>/api/v1/auth/token/` - получение токена
>Метод запроса: POST


Запрос:
```json
{
    "username": "b.moldabekov",
    "password": "pass1234!!"
}
```

Ответ:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNzk0MTA5MCwiaWF0IjoxNzA3ODU0NjkwLCJqdGkiOiI4ZjA5Y2QyZGQzODk0NWQzOTE2MGZhY2U4MTExMTcyYiIsInVzZXJfaWQiOjF9.huPWJ3wVI_IKanq7QbtWllVkfeEtmCBf9_9kIy9ZwSo",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3ODU0OTkwLCJpYXQiOjE3MDc4NTQ2OTAsImp0aSI6Ijk0MmQ2MmQzZDNiZjRhZDc4MThjNDRkMDQ2MDY1M2ZhIiwidXNlcl9pZCI6MX0.rZ47w4sCuPzpmD98m5rBjrVJ72PlwQwhMXoagAcsNNA"
}
```
2. `<HOST>:<PORT>/api/v1/auth/register/` - регистрация пользователя
> Метод запроса: POST

Запрос:
```json
{
    "username": "",
    "password": "",
    "password2": "",
    "email": "",
    "first_name": "",
    "last_name": ""
}
```

Ответ:
```json
{
    "username": "",
    "email": "",
    "first_name": "",
    "last_name": ""
}
```

3. `<HOST>:<PORT>/api/v1/auth/token/refresh/` - обновление токена
> Метод запроса: POST
>
> Запрос:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNzU3MTM4OCwiaWF0IjoxNzA3NDg0OTg4LCJqdGkiOiJhYjNmZWViYjQ4NTU0Y2YxOGJlMjA5YjQ5OGVkZTgzNyIsInVzZXJfaWQiOjF9.9e59n32kDB7LLiT499vCMspo8CS3R65xlD-tR83xchQ"
}
```
> Ответ:
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3NDg1NDYxLCJpYXQiOjE3MDc0ODQ5ODgsImp0aSI6IjljNzFlYTMyMDhiZTQ1MDA5OWY4NDMwM2EzOTI1MDdhIiwidXNlcl9pZCI6MX0.psNXhFCmMi3QsCXErCE_NC7py1KTP_0nhDLnbutO9dc"
}
```