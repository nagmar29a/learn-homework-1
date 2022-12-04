"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
  if type(first) is not str or type(second) is not str:
    return 0
  elif first == second:
    return 1
  elif len(first) > len(second) and 'learn' not in second:
    return 2
  elif first != second and 'learn' in second:
    return 3
    
if __name__ == "__main__":
  first = 'test'
  second = 1241
  print(main())
  first = 'test'
  second = 'test'
  print(main())
  first = 'testtesttest'
  second = 'test'
  print(main())
  first = 'testtesttest'
  second = 'learn'
  print(main())
