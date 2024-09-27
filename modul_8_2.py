class Numb:
    def personal_sum(self, numbers):
        result = 0
        incorrect_data = 0
        for i in numbers:
            try:
             result += i
            except TypeError:
                incorrect_data += 1
                print(f"В данных имееться вот эта ошибка: {i}")
        return result, incorrect_data
    def calculate_average(self, numbers):
        try:
            result, incorrect_data = self.personal_sum(numbers)
            minus = len(numbers) - incorrect_data
            Result = result/minus
            return Result


        except (ZeroDivisionError, UnboundLocalError ) as axc :
            print(f"В Вашем коде появился 0 и вывел вот эту ошибку {axc}")
            return 0
        except TypeError:
            print(f"В numbers записан некорректный тип данных ")
            return





print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
