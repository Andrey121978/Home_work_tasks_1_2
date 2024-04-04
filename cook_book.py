def get_cook_book(file):
    array_none = []
    cook_list = []
    cook_book = {}
    with open(file, encoding='utf8') as f:
        for line in f:
            if len(line.strip()) != 0:
                array_none.append(line.strip())
                cook_list.append(array_none)
            else:
                array_none = []
    for dishes in cook_list:
        ingridient_list = []
        for idx in range(2, len(dishes)):
            ingridient_list.append(dishes[idx].split(' | '))
        cook_book[dishes[0]] = ingridient_list
    for dishes in cook_book.values():
        for idx in range(len(dishes)):
           dishes[idx] = dict(ingredient_name=dishes[idx][0], quantity=int(dishes[idx][1]), measure=dishes[idx][2])

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book('recipes.txt')
    shop_list_by_dishes = {}
    for key, values in cook_book.items():
        if key in dishes:
            for ingrts in values:
                if ingrts['ingredient_name'] in shop_list_by_dishes.keys():
                    shop_list_by_dishes[ingrts['ingredient_name']]['quantity'] = shop_list_by_dishes[ingrts['ingredient_name']]['quantity'] + ingrts['quantity'] * person_count
                else:
                    shop_list_by_dishes[ingrts['ingredient_name']] = dict(measure=ingrts['measure'], quantity=ingrts['quantity'] * person_count)
    return shop_list_by_dishes

# print(get_cook_book('recipes.txt'))
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))
