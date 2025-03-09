people_info = {
    'Oraora': {'profession': 'QAEngineer', 'salary': 50000},
    'Stesia': {'profession': 'Bulochka', 'salary': 55000},
    'MarkDelta': {'profession': 'Barabanila', 'salary': 45000},
    'SnoopGogg': {'profession': 'WeedSmoker', 'salary': 40000},
    'Eminem': {'profession': 'RapGod', 'salary': 60000}
}


def check_list(dick):
    if 'MarkDelta' in people_info.keys():
        raise ValueError('Value Errorchik')


try:
    check_list(people_info)
except ValueError as ve:
    print(ve)


# Якщо > 0 true, Якшо < 0 False, if = 0  raise exeption
def check_sum(n1: int, n2: int):
    result = n1 + n2

    if result == 0:
        raise ArithmeticError("Arrif Error Comed")

    if result > 0:
        return True
    elif result < 0:
        return False




print(check_sum(5, 5))

list_blablabla = [('t1', True), ('t2', False), ('t3', True)]

empty_set = set()
empty_set.add('oragne')
empty_set.add('banana')
print(empty_set)
