# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archiv():
    """About class"""
    __instance = None

    def __init__(self, text: str, num: int):
        """Added the text and num parameters."""
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.text)
            cls.__instance.text_list.append(cls.__instance.num)
        return cls.__instance

    def __str__(self):
        return f' Экземпляр класса = {self.text}, {self.num}'

    def __repr__(self):
        return f' Экземпляр = {self.text}, {self.num}'


arch1 = Archiv('Ya', 2)
print(arch1.text_list)
print(arch1.num_list)

arch2 = Archiv('Ya', 3)
print(arch1.text_list)
print(arch1.num_list)

arch3 = Archiv('Yaa', 4)
print(arch1.text_list)
print(arch1.num_list)

print(arch1)
print(repr(arch1))
print(Archiv.__doc__)
print(arch1.__init__.__doc__)