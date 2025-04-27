def sum_list_recursive(lst):
    """
    Обчислює суму елементів списку рекурсивно.
    
    Аргументи:
    lst -- список чисел
    
    Повертає:
    Суму всіх елементів у списку
    """
    if not isinstance(lst, list):
        raise TypeError("Потрібно ввести список чисел.")
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])
