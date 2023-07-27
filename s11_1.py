# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
from time import time


class My_str(str):
    """About class"""
    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance
str1 = My_str('Hello', 'Ya')

print(str1.time)
print(str1.author)
print(My_str.__doc__)