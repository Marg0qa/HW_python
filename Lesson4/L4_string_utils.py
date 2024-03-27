class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """
    print("start")
    def capitilize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
        Пример: `capitilize("skypro") -> "Skypro"`
        """
        return string.capitilize()
    
    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть
        Пример: `trim("   skypro") -> "skypro"`
        """
        whitespace = " "
        while (string.startswith(whitespace)):
            string = string.removeprefix(whitespace)
        return string
    
    def to_list(self, string: str, delimeter = ",") -> list[str]:
        """
        Принимает на вход текст с разделителем и возвращает список строк. \n
        Параметры: \n 
            `string` - строка для обработки \n
            `delimeter` - разделитель строк. По умолчанию запятая (",") \n
        Пример 1: `to_list("a,b,c,d") -> ["a", "b", "c", "d"]`
        Пример 2: `to_list("1:2:3", ":") -> ["1", "2", "3"]`
        """
        if(self.is_empty(string)):
            return []
        
        return string.split(delimeter)

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n 
        Параметры: \n 
            `string` - строка для обработки \n
            `symbol` - искомый символ \n
        Пример 1: `contains("SkyPro", "S") -> True`
        Пример 2: `contains("SkyPro", "U") -> False`
        """
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass

        return res
    
    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки \n 
        Параметры: \n 
            `string` - строка для обработки \n
            `symbol` - искомый символ для удаления \n
        Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
        Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
        """
        if(self.contains(string, symbol)):
            string = string.replace(symbol, "")    
        return string
            
    def starts_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n 
        Параметры: \n 
            `string` - строка для обработки \n
            `symbol` - искомый символ \n
        Пример 1: `starts_with("SkyPro", "S") -> True`
        Пример 2: `starts_with("SkyPro", "P") -> False`
        """
        return string.startswith(symbol)

    def end_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n 
        Параметры: \n 
            `string` - строка для обработки \n
            `symbol` - искомый символ \n
        Пример 1: `end_with("SkyPro", "o") -> True`
        Пример 2: `end_with("SkyPro", "y") -> False`
        """
        return string.endswith(symbol)
    
    def is_empty(self, string: str) -> bool:
        """
        Возвращает `True`, если строка пустая и `False` - если нет \n 
        Пример 1: `is_empty("") -> True`
        Пример 2: `is_empty(" ") -> True`
        Пример 3: `is_empty("SkyPro") -> False`
        """
        string = self.trim(string)
        return string == ""
    
    def list_to_string(self, lst: list, joiner=", ") -> str:
        """
        Преобразует список элементов в строку с указанным разделителем \n 
        Параметры: \n 
            `lst` - список элементов \n
            `joiner` - разделитель элементов в строке. По умолчанию запятая (", ") \n
        Пример 1: `list_to_string([1,2,3,4]) -> "1, 2, 3, 4"`
        Пример 2: `list_to_string(["Sky", "Pro"]) -> "Sky, Pro"`
        Пример 3: `list_to_string(["Sky", "Pro"], "-") -> "Sky-Pro"`
        """
        string = ""
        length = len(lst)
        
        if length == 0: 
            return string 
        
        for i in range(0, length-1):
            string += str(lst[i]) + joiner
        
        return string + str(lst[-1])
    
    print("stop")
    
    
    
#     Похоже, что Ваша реализация метода `list_to_string` может привести к ошибке при пустом списке `lst`, так как Вы сначала инициализируете `string` пустой строкой и затем добавляете элементы списка к этой строке. Однако, если список пустой, то Вы сразу возвращаете пустую строку `string`, не учитывая разделитель `joiner`. Рекомендую добавить проверку на пустой список и вернуть пустую строку сразу, если список пустой. 

# Вот исправленный вариант метода `list_to_string`:

# ```python
# def list_to_string(self, lst: list, joiner=", ") -> str:
#     if not lst:
#         return ""
    
#     return joiner.join(map(str, lst))
# ```

# Этот вариант более короткий и использует метод `join` для объединения элементов списка в строку с разделителем. Также он обрабатывает случай пустого списка корректно.

# ОШИБКИ
# В коде класса StringUtils есть несколько ошибок:

# 1. В методе `delete_symbol` необходимо добавить документацию и примеры использования.
# 2. В методе `end_with` опечатка в названии метода, должно быть `ends_with` вместо `end_with`.
# 3. В методе `list_to_string`, при объединении элементов списка в строку, необходимо учитывать, что разделитель `joiner` не должен добавляться после последнего элемента списка.

# Помимо этого, рекомендуется добавить тесты для всех методов класса StringUtils, чтобы убедиться в их корректной работе.


# Для тестирования функций класса `StringUtils` можно написать следующие тесты:

# 1. **Позитивные тесты**:
#    - Проверка функции `capitalize` на строке, которая начинается с маленькой буквы.
#    - Проверка функции `trim` на строке с пробелами в начале.
#    - Проверка функции `to_list` на строке с разделителем, который есть в строке.
#    - Проверка функции `contains` на строке, где символ присутствует.
#    - Проверка функции `delete_symbol` на удаление одиночного символа из строки.
#    - Проверка функции `starts_with` на строке, которая начинается с заданного символа.
#    - Проверка функции `end_with` на строке, которая заканчивается заданным символом.
#    - Проверка функции `is_empty` на пустой строке и на строке с пробелом.
#    - Проверка функции `list_to_string` на преобразование списка в строку с разделителем.

# 2. **Негативные тесты**:
#    - Проверка функции `capitalize` на пустой строке.
#    - Проверка функции `trim` на пустой строке.
#    - Проверка функции `to_list` на пустой строке.
#    - Проверка функции `contains` на символ, которого нет в строке.
#    - Проверка функции `delete_symbol` на удаление символа, которого нет в строке.
#    - Проверка функции `starts_with` на строке, которая не начинается с заданного символа.
#    - Проверка функции `end_with` на строке, которая не заканчивается заданным символом.
#    - Проверка функции `is_empty` на строке, которая не пустая.
#    - Проверка функции `list_to_string` на пустом списке.

# Такие тесты позволят проверить работу каждой функции в различных сценариях.
