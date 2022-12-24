"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

#def main():
    
    #Эта функция вызывается автоматически при запуске скрипта в консоли
   # В ней надо заменить pass на ваш код
    
    #pass
    
#if __name__ == "__main__":
#    main()


products_info = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def count_products_sales(sold_info):
  sales_sum = 0
  for sales in sold_info:
    sales_sum = sales_sum + sales
  return(sales_sum)

all_sum_sales = 0

for one_phone in products_info:
  print(one_phone['product'])
  sum_sales = count_products_sales(one_phone['items_sold'])
  print(f'Сумма продаж {sum_sales}')
  average_sum_one_phone = sum_sales / len(one_phone['items_sold'])
  print(f'Средние продажи {round(average_sum_one_phone, 2)}')
  all_sum_sales = all_sum_sales + sum_sales
  
print(f'Всего продаж товаров {all_sum_sales}')
print(f'Среднее количество продаж всех товаров {all_sum_sales / len(products_info)}')
