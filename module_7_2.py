# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
# strings - список строк для записи.

'''
    Функция выполняет:
    Записывает в файл file_name все строки из списка strings, каждая на новой строке.
    Возвращает словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
    а значением - записываемая строка.
    Для этого создаем переменную "strings_positions" с пустым словарем, куда будем добавлять значения.
    Создадим переменную "line", где укажем номер строки откуда будет начинаться считывание, начало с 1 строки.
    Создадим переменную "file", в которой будем сохранять результат записи в открытый("open") файл.
    Пройдем циклом "for", чтобы перебрать строки и записать в переменную "string".
    Создадим переменную для получения номера байта начала строки, используя метод "tell()".
    Записываем в переменную "file" все строки из переменной "string", каждую на новую строку используя ("\n").
    Записываем в словарь кортеж с номером строки и байтом начала строки.
    Пройдем по всем строкам фала (line+=1).
    Закрываем файл "close()", и возвращаем (return) сформированный словарь "strings_positions".
'''
def custom_write(file_name, strings):
    strings_positions = {}
    line = 1
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        byte_line = file.tell()
        file.write(f'{string}\n')
        strings_positions[(line, byte_line)] = string
        line+=1
    file.close()
    return strings_positions

if __name__ == '__main__':

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

    result = custom_write('test.txt', info)
    for elem in result.items():
      print(elem)

