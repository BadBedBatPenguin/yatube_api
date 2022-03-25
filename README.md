### Yatube API

REST API к соцсети [Yatube](https://github.com/BadBedBatPenguin/Yatube)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```Shell
git clone https://github.com/BadBedBatPenguin/yatube_api.git
```

```Shell
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```Shell
python3 -m venv env
```

```Shell
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```Shell
python3 -m pip install --upgrade pip
```

```Shell
pip install -r requirements.txt
```

Выполнить миграции:

```Shell
python3 manage.py migrate
```

Запустить проект:

```Shell
python3 manage.py runserver
```

### Документация

Докуентацию к API можно посмотреть после запуска сервера [здесь](https://127.0.0.1:8000/redoc/)
