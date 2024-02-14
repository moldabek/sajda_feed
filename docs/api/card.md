# API для взаимодействия с данными в базе

1. `<HOST>:<PORT>/api/v1/` - отображение ленты в json формате
>Метод запроса: GET

> Параметры запроса: `access_token: str(optional)`

Запрос: Не передается

Ответ:
```json
{
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 2,
      "card_type": "QURAN_AYAH",
      "title": "Al-Fatiha",
      "content": "In the name of Allah, the Entirely Merciful, the Especially Merciful.",
      "additional_info": "The Opening. Surah 1. Ayah 1",
      "arabic_text": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
      "content_url": null,
      "picture": null,
      "description": null,
      "date": null,
      "repeat": "daily",
      "repeat_days": null,
      "active": true,
      "created_at": "2024-02-12T12:28:41.677826Z",
      "play_in_app": false
    }
  ]
}
```
2. `<HOST>:<PORT>/api/v1/{id}` - отображение ленты в json формате
> Метод запроса: GET

> id - идентификатор карточки

> Параметры запроса: `access_token: str(optional)`

3. `<HOST>:<PORT>/api/v1/{id}/` - создание взаимодействия с карточкой
> Метод запроса: POST
>
> id - идентификатор карточки
>
> interaction_type - тип взаимодействия с карточкой(like, hide, dhikr)
> 
> Параметры запроса: `access_token: str(required); interaction_type: str(required)`
> 
> Запрос:
```json
{
  "interaction_type": "like"
}
```
> Ответ:
```json
{
  "status": "ok"
}
```