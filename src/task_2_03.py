# Создать список из двух элементов.
# Создать кортеж из двух элементов.
# Создать словарь с одной парой. Ключ - кортеж, значение - список
# Создать словарь с одной парой. Ключ - список, значение - кортеж

l = ['test', 'world']
t = (15, 25,)
d = {
    ('product',): ['phone'],
}

d2 = {repr([1, 2, 3]): 'value'}
print(d2)

# Списки не могут быть использованы в качестве ключей в словаре в виду того, что изменяемые коллекции не хешируются
# Ключи должны быть неизменными для хеширования