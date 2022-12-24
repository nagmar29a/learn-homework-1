"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""



def hello_user():
  print('Как дела?')
  answer = input()
  good = 'Хорошо'
  while answer != good:
    print('Как дела?')
    answer = input()

if __name__ == "__main__":
    hello_user()
    