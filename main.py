from pprint import pprint
import os
path = os.path.join(os.getcwd(), 'file_test.txt')



with open(path) as data:
    cook_book = {}
    for string_all in data:
        name_food = string_all.strip()
        counter = int(data.readline().strip())
        temp = []
        for string in range(counter):
            ingredient_name, quantity, measure = data.readline().strip().split(' | ')
            temp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[name_food] = temp
        data.readline().strip()
# pprint(cook_book)

# ________________function___________________
pprint(int(cook_book['Фахитос'][0]['quantity']))


def get_shop_list_by_dishes(dishes, person_count):
    ingredient_check = {}
    for dish in dishes:
        for count in range(len(cook_book.keys())):
            if dish == (list(cook_book.keys()))[count]:
                for string1 in range(len(cook_book[dish])):
                    ingredient_check[cook_book[dish][string1]['ingredient_name']] = {'measure': cook_book[dish][string1]['measure'], 'quantity': int(cook_book[dish][string1]['quantity'])*person_count}
    return ingredient_check


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))




