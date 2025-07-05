import os

# встановлення потрібних модулів
os.system("pip install -r requirements.txt")
# перевірка, які модулі реалььно встановлені у віртуальному оточенні
os.system("pip freeze > installed_packages.txt")

try:
    import django
    import environ
    print("All packages imported successfully.")
except ImportError as e:
    print("ImportError:", e)

# накатуємо міграційні скріпти джанго
os.system("python3 manage.py migrate")
