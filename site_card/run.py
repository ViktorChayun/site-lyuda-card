import os

wgi = "manage.py"

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
os.chdir('/home/hypnocon/site2')
cmd = f"python3 {wgi} migrate"
os.system(cmd)

# збираємо всі статичні файли
cmd = f"python3 {wgi} collectstatic"
os.system(cmd)
