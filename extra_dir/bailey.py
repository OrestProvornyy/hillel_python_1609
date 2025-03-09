# # import math
# # import random
# #
# # # my_set = {1,7,3,4}
# # # print(len(my_set))
# #
# # users = [
# #     {'name': 'Den', 'math': 50, 'phil': 60},
# #     {'name': 'Alex', 'math': 50, 'phil': 60},
# #     {'name': 'Jack', 'math': True, 'phil': 60},
# #     {'name': 'Ivan', 'math': 50, 'phil': None},
# #     {'name': 'Kim', 'phil': 45},
# #
# # ]
# #
# #
# # def test_count_data(user_list):
# #     for k in user_list:
# #         try:
# #             str_1 = 'Mark klasnui pacan'
# #             str_2 = '234'
# #             result = int(str_1) + int(str_2)
# #             # assert k['name'] + k['name'] > 0
# #             print(k['god'], k['math'] + k['phil'])
# #
# #         except ValueError as valer:
# #
# #             print(f'Qwe {valer}')
# #
# #         except KeyError as asd:
# #
# #             print(f'Cant get key {asd} for {k}')
# #             print(asd)
# #
# #         except TypeError as asdf:
# #
# #             print(f'Found None but its not a bug, continue {k}')
# #             print(asdf)
# #
# #
# # test_count_data(users)
# #
# # # def connect_to_db():
# # #     if random.random() > 0.5:
# # #         raise ConnectionError("Cant connect")
# # #
#
#
# #
# #
# #
# # Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# #
# # [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# #
# # Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# #
# # Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# #
# # Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# #
# # Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”
# #
# # my_arr = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
# #
# #
# # def sum_of_elemets():
# #     new_arr = [x.split(',') for x in my_arr]
# #     print(new_arr)
# #
# #     for element in new_arr:
# #         try:
# #             int_arr = [int(el) for el in element]
# #             print(int_arr)
# #             print(sum(int_arr))
# #
# #         except ValueError as e:
# #             print(f'\nCant parse {e}')
# #
# #
# # sum_of_elemets()
#
# #
# # try:
# #     print('asd')
# #
# # except TypeError as e:
# #     pass
# #

users = [
    {'name': 'Petro', 'scores': {'math': 'fifty', 'phil': 59, 'lit': 'zero'}},
    {'name': 'Den', 'scores': {'math': 50, 'phil': 60, 'lit': 60}},
    {'name': 'Alex', 'scores': {'math': 5099, 'phil': 60, 'lit': 30}},
    {'name': 'Jack', 'scores': {'math': True, 'phil': 60, 'lit': 80}},
    {'name': 'Ivan', 'scores': {'math': 50, 'phil': None, 'lit': 75}},
    {'name': 'Kim', 'scores': {'phil': 45}},
    {'name': 'KimChiIn', 'scores': {}}
]


def get_user_score(user):
    scores = user.get('scores')
    sum = 0

    # Перебираємо всі предмети і їх оцінки
    for s in scores:
        try:
            # Перевіряємо, чи є оцінка числом, і додаємо до загальної суми
            sum += scores[s]
        except TypeError:
            # Якщо оцінка некоректна, виводимо повідомлення і продовжуємо цикл
            print(f'Incorrect data for {s}')

    try:
        # Перевіряємо, чи можна поділити на кількість оцінок
        result = sum / len(scores)
    except ZeroDivisionError:
        print(f'No data for user {user["name"]}')
        return 0

    else:  # якщо не було помилок
        print('There is no Errors')

    finally:  # буде виконуватись завжди
        print(f'Finally: User has score in {sum}')

    return result  # Повертаємо результат


for user in users:
    print(f'User name is {user["name"]}')
    print(f'User score is {get_user_score(user)}')
    print('-' * 29)

# qwerty = 'qwerty bitch ass hole ass '
#
# new_qwert = qwerty.replace('ass', 'pussy', 2)
#
# print(new_qwert)
#
# new_qwerе_2 = qwerty.strip()
#
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
#
# print(thistuple)
#
# maza_fuck_tuple = 1, 2, 3, "Big Dick", True, "Very True"
# print(type(maza_fuck_tuple))
