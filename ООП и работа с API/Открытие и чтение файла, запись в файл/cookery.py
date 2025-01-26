def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book('recipes.txt')
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print(f'Блюда \"{dish}\" нет в кулинарной книге!')

        else:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count

                else:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                'quantity': ingredient['quantity'] * person_count}

    return shop_list


def get_cook_book(file_name):
    with open(f'{file_name}', 'r', encoding='utf-8') as file:
        cook_book = {}
        content = file.read().split('\n')
        for i in range(len(content)):
            if content[i].isdigit():
                recipe = []
                for j in range(int(content[i])):
                    recipe += [{'ingredient_name': x,
                                'quantity': int(y),
                                'measure': z} for x, y, z in [content[i + j + 1].split(' | ')]]
                cook_book[content[i - 1]] = recipe

    return cook_book


if __name__ == '__main__':
    print('Книга рецептов:\n', get_cook_book('recipes.txt'), '\n', sep='')

    print('Список покупок:\n', get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5), sep='')
