# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
# Значение должно быть скопировано из настроек или документации сервиса, к которому предоставляется доступ.
# Пример значения: "https://api.example.com"
URL_SERVICE = "https://479d132e-00a2-4dd6-a34d-a58d7ce80239.serverhub.praktikum-services.ru"

LOG_MAIN_PATH = "/api/logs/main/"
USERS_TABLE_PATH = "/api/db/resources/user_model.csv"
# DOC_PATH содержит путь к документации веб-сервиса.
# Этот путь используется для формирования полного URL пути к документации, добавляя его к базовому URL сервиса.
# В результате получится что-то вроде "https://api.example.com/docs/"
DOC_PATH = "/docs/"

CREATE_USER_PATH = "/api/v1/users/"
PRODUCTS_KITS_PATH = "/api/v1/products/kits/"