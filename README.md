**SITE-AUCTION: Платформа для покупки/продажи аккаунтов**
*Краткое описание*
Проект представляет собой веб-приложение-аукцион на Django, позволяющее пользователям регистрироваться, публиковать лоты (продавать аккаунты) и участвовать в торгах. Система использует PostgreSQL в качестве СУБД, Docker & Docker Compose для контейнеризации, а также Nginx и Uvicorn для деплоя и обратного проксирования HTTP-запросов.

MYBESTPROJECT/
├── .gitignore
├── README                  ← Текущий файл
├── Dockerfiles/
│   ├── nginx/
│   │   └── nginx.conf      ← Конфигурация Nginx
│   └── uvicorn/
│       └── Dockerfile      ← Dockerfile для Uvicorn (ASGI-сервера)
└── kursov/                 ← Основная директория Django-проекта
    ├── .dockerignore
    ├── .env                ← Файл переменных окружения
    ├── compose.yml         ← Docker Compose для локального запуска
    ├── Dockerfile          ← Dockerfile приложения (Django + Uvicorn)
    ├── manage.py
    ├── requirements.txt    ← Python-зависимости
    ├── app/                ← Django-приложение
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── urls.py
    │   ├── au/             ← Подприложение “Auction” (логику аукциона)
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── main/           ← Подприложение “Main” (общие страницы: главная, о нас, правила)
    │   │   ├── css/
    │   │   ├── js/
    │   │   ├── urls.py
    │   │   └── views.py
    │   └── migrations/
    ├── conf/               ← Конфигурация Django-проекта
    │   ├── asgi.py
    │   ├── settings.py     ← Основные настройки (ссылки на .env)
    │   ├── urls.py
    │   └── wsgi.py
    └── templates/          ← Шаблоны (Jinja-like)
        ├── au/
        │   ├── index.html
        │   ├── login.html
        │   ├── profile.html
        │   └── register.html
        └── main/
            ├── base.html
            └── index.html

**🛠 Технологии и стек**
-Язык и фреймворк: Python 3.x, Django 5.2
-База данных: PostgreSQL
-Сервер приложений: Uvicorn (ASGI)
-Веб-сервер / обратное проксирование: Nginx
-Контейнеризация и оркестрация (локально): Docker, Docker Compose
-Клиентские ресурсы: CSS (стили в app/main/css/), JavaScript (в app/main/js/), HTML-шаблоны (в templates/)
-Авторизация: встроенная auth-система Django (регистрация, вход/выход, смена пароля)

**🔧 запуск**
Примечание. Все действия нужно выполнять в директории MYBESTPROJECT/kursov/.
они

```DJANGO_SECRET_KEY="ваш_секретный_ключ_Django"
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_INTERNAL_IPS=127.0.0.1

POSTGRES_USER=<имя_пользователя_PostgreSQL>
POSTGRES_PASSWORD=<пароль_PostgreSQL>
POSTGRES_DB=<имя_БД_PostgreSQL>
PG_USER=<имя_пользователя_PostgreSQL>
PG_PASS=<пароль_PostgreSQL>
PG_LINK=<хост_БД_или_адрес_контейнера>
DJANGO_DEBUG=1 включает режим отладки (DEV). В production ставьте 0.```

Параметры POSTGRES_* используются при запуске через Docker Compose (имитируют локальный контейнер базы).

Параметры PG_* считываются прямо из settings.py для подключения Django к БД.

Установить зависимости
Если вы не используете Docker, можно завести виртуальное окружение вручную:

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
Однако рекомендуется использовать Docker Compose (см. ↓).

Запуск контейнеров через Docker Compose
В корне (рядом с compose.yml) выполнить:

docker-compose up -d --build
PostgreSQL (сервис db)
Django + Uvicorn (сервис web)
Nginx (сервис nginx) — проксирует запросы и отдаёт статику.
После успешного билда и старта, приложение будет доступно по адресу:

**🚀 Использование**
Регистрация и вход
Перейдите на http://localhost/au/register/ для создания учётной записи.
После регистрации зайдите на http://localhost/au/login/ для входа.
Личный кабинет
После входа вы попадаете на http://localhost/au/profile/ (страница профиля).
Здесь можно изменить личные данные или перейти к созданию/просмотру лотов.
Просмотр и участие в аукционах
Главная страница аукциона: http://localhost/au/ (список доступных лотов).
Выберите лот для просмотра деталей и ставки.
Основные URL-приложения
/main/ → Главная («glavnaya») и общие страницы (About, Terms, Privacy).
/au/ → Вся логика аукциона: вход/регистрация, создание лотов, ставки.
Админка Django
Доступна по умолчанию на http://localhost:8000/admin/ (логин — созданный superuser).
Через админку можно управлять пользователями, лотами, ставками и т. д.

**🔎 Основные компоненты и функции**
Модели (app/models.py)
ExampleModel – демо-модель (пример).
CustomUser (если реализован в проекте) – расширенная модель пользователя.
Product / Lot – модель лота (аккаунта), который выставляется на продажу.
Bid – ставки пользователей по лоту.
Order / Purchase – информация о совершённых сделках (после завершения аукциона).
Примечание: в текущей реализации некоторые из перечисленных моделей могут отсутствовать или требовать доработки.
Views (app/au/views.py)
index – страница списка лотов.
login, register – формы аутентификации/регистрации.
profile – личный кабинет пользователя.
create_lot / place_bid / auction_detail – функционал создания лотов и участия в торгах.
Шаблоны (HTML/CSS/JS)
Каталог templates/au/ содержит шаблоны для страниц аукциона:
index.html, login.html, register.html, profile.html, edit_profile.html, password_change.html.
В templates/main/ лежат базовые шаблоны сайта: base.html, index.html (главная информационная страница).
Статические файлы
CSS: app/main/css/ (например, base.css, index.css).
JS: app/main/js/index.js.
Docker & Nginx
Dockerfiles/uvicorn/Dockerfile – билд образа для запуска Django через Uvicorn (ASGI).
Dockerfiles/nginx/nginx.conf – конфигурация Nginx: прокси для ASGI, раздача /static/, работа с SSL (при необходимости).
compose.yml – orchestrator для трёх сервисов: web (Django+Uvicorn), db (PostgreSQL), nginx.



