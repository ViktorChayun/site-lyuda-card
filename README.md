# site-lyuda-card

+ сайт візітівка
+ одразу з сайту перейти в телеграм чи вайбер і написати напряму
- заповнити анкетку - кнопочку, замовити зворотній звязок
- додати форму запису на консультацію
+ розширити розділи 
    - блог
    + FAQ
    - відгуки
+ додати картинки диплому в секції про себе
+ на головнку вставити фон як картинку
+ півдсвідка карточки при наведенні
+ додати рамку синю + підсвідтку + тінь голубувату
+ Pages:
    + home
        + змістити текст ще трохи вправо
    + faq
        + лого для частих питань background-faq 2.jpg
        + прозорість в схлопнутому стані
    + services
    + about
+ Navbar
    + add logo
    + фільтр мова: укр/рус
        + base.html
        + home.html
        + service.html
        + faq.html
        + about.html
----------------------
перевірити як відкривається на мобільних
    мій
    Люди
запаблішити
оформити все в Docker для деплою
------------------------
Команди для генерації перекладів:
django-admin makemessages -l uk
django-admin makemessages -l ru


# редагуєш .po файли у locale/uk/LC_MESSAGES/django.po
    django-admin compilemessages

Переклади в .po файлах
Після додавання {% trans %} в шаблонах:

Виконай у терміналі:
    django-admin makemessages -l ru

Це згенерує файл перекладу:
    locale/ru/LC_MESSAGES/django.po

В ньому ти побачиш:
msgid "Головна"
msgstr ""
➡️ Впиши переклад:
msgid "Головна"
msgstr "Главная"

І так для всіх фраз.

Після редагування:
django-admin compilemessages


Альтернатива: Використати WSL (Linux-середовище в Windows)
Якщо ти вже використовуєш Windows Subsystem for Linux (WSL), просто виконай:

bash
Copy
Edit
sudo apt update
sudo apt install gettext
А тоді можеш запускати команду makemessages вже з Linux-середовища.



# як перегенерувати переклади?
1. виконай 
    django-admin makemessages -l ru
2. Додай переклади у файл locale/ru/LC_MESSAGES/django.po.
3. Згенеруй .mo файл:
    django-admin compilemessages
4. перезапусти сервер