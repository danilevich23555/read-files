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
            product_name, quantity, measure = data.readline().strip().split(' | ')
            temp.append({'product_name': product_name, 'quantity': quantity, 'measure': measure})
        cook_book[name_food] = temp
        data.readline().strip()

# ________________function___________________
def get_shop_list_by_dishes(dishes, person_count):
    check = {}
    for dish in dishes:
        for count in range(len(cook_book.keys())):
            if dish == (list(cook_book.keys()))[count] and dishes.count(dish) == 1:
                for string1 in range(len(cook_book[dish])):
                    check[cook_book[dish][string1]['product_name']] = {'measure': cook_book[dish][string1]
                    ['measure'], 'quantity': int(cook_book[dish][string1]['quantity'])*person_count}
            elif dish == (list(cook_book.keys()))[count] and dishes.count(dish) > 1:
                for string1 in range(len(cook_book[dish])):
                    check[cook_book[dish][string1]['product_name']] = {'measure': cook_book[dish][string1]
                    ['measure'],'quantity': int(cook_book[dish][string1]['quantity']) * dishes.count(dish)*person_count}
    return check
# _________________________________function result___________________________________
pprint(get_shop_list_by_dishes(['Омлет'], 2))
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1))







