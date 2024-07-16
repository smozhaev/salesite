# Курсовая работа: Агрегатор скидок

Этот проект представляет собой агрегатор скидок, реализованный в рамках курсовой работы.

## Установка приложения

Приложение можно склонировать:

```bash
git clone git@github.com:smozhaev/salesite.git
```

Затем необходимо добавить создать пару ключ-значение в Google Cloud для OAuth 2.0 и в папке app создать два файла для авторизации с помощью OAuth 2.0:

```bash
echo "клиент Google OAuth без кавычек" > client.txt
echo "пароль Google OAuth без кавычек" > secret.txt
```

## Запуск сервера

Для запуска сервера перейдите в корневую папку проекта и выполните следующую команду:

```bash
docker-compose up -d
```

## Django API

Ссылка на API: [/catalog/api/v1/](localhost:8000/catalog/api/v1/)

## Админка

Ссылка на панель администратора: [/admin](localhost:8000/admin/)

## Swagger

Ссылка на документацию Swagger: [/catalog/swagger](localhost:8000/catalog/swagger/)

