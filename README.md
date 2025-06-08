# JSON2Video - Установка и настройка

Подробное руководство по установке и настройке проекта для автоматического создания видео с использованием JSON2Video API.

## 📋 Системные требования

- **Python**: версия 3.8 или выше
- **FFmpeg**: для конвертации видеофайлов
- **Операционная система**: Windows, macOS, или Linux
- **Интернет-соединение**: для работы с API и загрузки медиафайлов
- **Свободное место**: минимум 1 ГБ для временных файлов и выходных видео

## 🔑 Получение API ключа

1. Зарегистрируйтесь на сайте [JSON2Video](https://json2video.com)
2. Войдите в личный кабинет
3. Перейдите в раздел "API Keys" или "Настройки API"
4. Создайте новый API ключ или скопируйте существующий
5. Сохраните ключ в безопасном месте - он понадобится для настройки

## 🐍 Установка Python

### Windows

1. **Загрузите Python**:
   - Перейдите на https://python.org/downloads/
   - Скачайте последнюю стабильную версию Python 3.8+
   - Запустите установщик

2. **Настройте установку**:
   - ✅ Обязательно отметьте "Add Python to PATH"
   - ✅ Выберите "Install for all users" (опционально)
   - Нажмите "Install Now"

3. **Проверьте установку**:
   ```cmd
   python --version
   pip --version
   ```

### macOS

1. **Через Homebrew (рекомендуется)**:
   ```bash
   # Установите Homebrew, если не установлен
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Установите Python
   brew install python
   ```

2. **Или скачайте с официального сайта**:
   - Загрузите установщик с python.org
   - Запустите .pkg файл и следуйте инструкциям

3. **Проверьте установку**:
   ```bash
   python3 --version
   pip3 --version
   ```

### Linux (Ubuntu/Debian)

1. **Обновите систему**:
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

2. **Установите Python**:
   ```bash
   sudo apt install python3 python3-pip python3-venv -y
   ```

3. **Проверьте установку**:
   ```bash
   python3 --version
   pip3 --version
   ```

## 🎬 Установка FFmpeg

FFmpeg необходим для конвертации и обработки видеофайлов.

### Windows

**Вариант 1: Через Chocolatey (рекомендуется)**
```cmd
# Установите Chocolatey, если не установлен
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Установите FFmpeg
choco install ffmpeg -y
```

**Вариант 2: Ручная установка**
1. Скачайте FFmpeg с https://ffmpeg.org/download.html#build-windows
2. Распакуйте архив в `C:\ffmpeg`
3. Добавьте `C:\ffmpeg\bin` в переменную PATH:
   - Откройте "Параметры системы" → "Дополнительные параметры системы"
   - Нажмите "Переменные среды"
   - В разделе "Системные переменные" найдите "Path"
   - Добавьте новый путь: `C:\ffmpeg\bin`

### macOS

```bash
# Через Homebrew
brew install ffmpeg

# Или через MacPorts
sudo port install ffmpeg
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg -y
```

### Проверка установки FFmpeg

```bash
ffmpeg -version
```

Вы должны увидеть информацию о версии FFmpeg.

## 📁 Настройка проекта

### 1. Клонирование или загрузка проекта

```bash
# Если проект в Git репозитории
git clone <url-репозитория>
cd json2video-project

# Или создайте папку и скопируйте файлы проекта
mkdir json2video-project
cd json2video-project
```

### 2. Создание виртуального окружения

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Вы должны увидеть `(venv)` в начале командной строки.

### 3. Установка зависимостей Python

```bash
pip install -r requirements.txt
```

Если файл `requirements.txt` отсутствует, установите зависимости вручную:
```bash
pip install pydantic pydantic-settings python-dotenv requests
```

### 4. Настройка переменных окружения

1. **Создайте файл .env**:
   ```bash
   # Скопируйте шаблон
   cp .env.example .env
   
   # Или создайте файл вручную
   touch .env  # на Linux/macOS
   # На Windows создайте файл через блокнот
   ```

2. **Отредактируйте .env файл**:
   ```env
   JSON2VIDEO_API_KEY=ваш_реальный_api_ключ_здесь
   JSON2VIDEO_BASE_URL=https://api.json2video.com/v2
   ```

   **Важно**: Замените `ваш_реальный_api_ключ_здесь` на настоящий API ключ от JSON2Video!

### 5. Создание папки для выходных файлов

```bash
mkdir output
```

## ✅ Проверка установки

### 1. Проверьте структуру проекта

Убедитесь, что у вас есть следующие файлы и папки:
```
json2video-project/
├── main.py
├── json2video/
│   ├── __init__.py
│   └── types.py
├── settings/
│   └── __init__.py
├── requirements.txt
├── .env
├── output/
└── venv/
```

### 2. Проверьте импорт модулей

```bash
python -c "from json2video import Movie, Scene, Image, Video, Audio, Subtitles; print('Импорт успешен!')"
```

### 3. Проверьте настройки

```bash
python -c "from settings import settings; print(f'API Key настроен: {bool(settings.json2video_api_key)}')"
```

### 4. Тестовый запуск

```bash
python main.py
```

Если все настроено правильно, вы увидите логи создания видео:
```
============= Start Task 1 =============
2025-06-08 12:00:00 - json2video - INFO - Create movie: {...}
2025-06-08 12:00:01 - json2video - INFO - Get movie abc123 status
2025-06-08 12:00:02 - json2video - INFO - abc123: processing
...
```

## 🚨 Решение проблем

### Ошибка "python не распознается"
- **Windows**: Переустановите Python с галочкой "Add to PATH"
- **macOS/Linux**: Используйте `python3` вместо `python`

### Ошибка "ffmpeg не найден"
- Проверьте установку: `ffmpeg -version`
- Перезапустите терминал после установки
- На Windows проверьте переменную PATH

### Ошибка "ModuleNotFoundError"
- Убедитесь, что виртуальное окружение активировано
- Переустановите зависимости: `pip install -r requirements.txt`

### Ошибка API (401 Unauthorized)
- Проверьте правильность API ключа в файле `.env`
- Убедитесь, что ключ активен в личном кабинете JSON2Video

### Ошибка "Permission denied" при создании папок
- **Linux/macOS**: Используйте `sudo` если необходимо
- **Windows**: Запустите терминал от имени администратора

## 🎯 Готово!

После успешной установки вы можете:
- Запускать готовые примеры из `main.py`
- Создавать собственные видео, модифицируя код
- Изучать документацию JSON2Video API для расширенных возможностей

Готовые видео будут сохраняться в папке `output/` в формате MP4.
