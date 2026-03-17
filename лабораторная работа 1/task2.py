# TODO Найдите количество книг, которое можно разместить на дискете

disk = 1.44 * 1024 * 1024
pages = 100
strings = 50
symbols = 25
one_symbol = 4
book = symbols * one_symbol * pages * strings
print("Количество книг, помещающихся на дискету:", int(disk//book))
