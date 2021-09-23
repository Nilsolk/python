
#ПДО 21 Гурьянов А.С
# Task1
# n = int(input())
# x = 1
# S = 0
# for x in range(n + 1):
#     S = S + x * x
#     x = x + 1
# print(S)

# Task2

# nums = [3, 7, -12, 22, 9, 44, 33, 6, -18, 22]
# x = sorted(nums)
# print(x)
# for i in x:
#     if i < 10:
#         nums.remove(i)
#     else:
#         continue
#
# print(nums)

# Task3

# companies = [['Apple', 2.2],
#              ['Microsoft', 1.6],
#              ['Amazon', 1.6],
#              ['Delta Electronics', 1.4],
#              ['Alphabet', 1.2],
#              ['Tesla', 0.8]]
# k=0
# x=len(companies)
# while k < x:
#     print('Капитализация компании', companies[k][0], 'составляет', companies[k][1], 'трлн. долларов')
#     k=k+1

cook_book = [
    ['салат',
     [
         ['картофель', 100, 'гр.'],
         ['морковь', 50, 'гр.'],
         ['огурцы', 50, 'гр.'],
         ['горошек', 30, 'гр.'],
         ['майонез', 70, 'мл.'],
     ]
     ],
    ['пицца',
     [
         ['сыр', 50, 'гр.'],
         ['томаты', 50, 'гр.'],
         ['тесто', 100, 'гр.'],
         ['бекон', 30, 'гр.'],
         ['колбаса', 30, 'гр.'],
         ['грибы', 20, 'гр.'],
     ],
     ],
    ['фруктовый десерт',
     [
         ['хурма', 60, 'гр.'],
         ['киви', 60, 'гр.'],
         ['творог', 60, 'гр.'],
         ['сахар', 10, 'гр.'],
         ['мед', 50, 'мл.'],
     ]
     ]
]
person=int(input())
for (name, items) in cook_book:
  print('\n',name.capitalize())
  for (ingredient, quantity, unit) in items:
    print(ingredient, quantity * person, unit)

#Мы поняли как работает, т. к. нашли в гугле, но сами не догадались
