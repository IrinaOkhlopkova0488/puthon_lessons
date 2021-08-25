#  *** Генератор паролей ***
# классы пишутся с большой буквы

import hashlib
from tkinter import Tk, Label, Entry, Button, StringVar

def hashing():
    """
    многострочный комментарий

    Функция хеширования
    :Принимает строку пароли и СОЛЬ
    :Возвращает хеш-строку
    """

    # прием строки человекочитаемой пароли с СОЛЬЮ
    pwd_str = pwd.get()  
    # кодирование в байт-строку
    byte_str = pwd_str.encode()
    # хеширование (применение хеш-функции из модуля hashlib)
    hash_str = hashlib.sha256(byte_str)  
    # преобразование хеш-строки спец типа в обычную строку типа str
    hex_str = hash_str.hexdigest()[:10]
    # передача захештрованной строки
    hash_pwd.set(hex_str)
    # print(hex_str)
    # print(type(hex_str))

# hashing("qwerty")

# объект окна
window = Tk()
window.title("генератор паролей свой")
# переменные класса ScringVar
pwd = StringVar()
hash_pwd = StringVar()

# виджет (компонент) текстовой метки
Label(text="Пароль:").grid(row=0, column=0, padx=5, pady=5) 
# виджет поля ввода
Entry(textvariable=pwd).grid(row=0, column=1, padx=5, pady=5)
# виджет кнопки
Button(text="Старт", command=hashing).grid(row=1, column=0, padx=5, pady=5)
# виджет поля вывода
Entry(textvariable=hash_pwd).grid(row=1, column=1, padx=5, pady=5)

# запуск программы (точкой входа программы)
window.mainloop()
