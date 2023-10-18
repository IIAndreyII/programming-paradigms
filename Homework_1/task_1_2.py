# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


def sort_list_imperative(list_num):
    for i in range(len(list_num) - 1):
        for j in range(len(list_num) - i - 1):
            if list_num[j] < list_num[j + 1]:
                list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]
    return list_num


numbers = [36, 78, 42, 27, 27, 14, 0, 98, 24, 67]
print(sort_list_imperative(numbers))


# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле


def sort_list_declarative(list_num):
    list_num.sort(reverse=True)
    return list_num


print(sort_list_declarative(numbers))
