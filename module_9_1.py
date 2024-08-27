# Введение в функциональное программирование
# Задача "Вызов разом"
def min_(int_list):
    return min(int_list)

def max_(int_list):
    return max(int_list)

def len_(int_list):
    return len(int_list)

def sum_(int_list):
    return len(int_list)

def sorted_(int_list):
    return sorted(int_list)

def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        res = function(int_list)
        result[function.__name__] = res
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
