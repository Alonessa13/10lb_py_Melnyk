def factorial_recursive(n):
    """
    Обчислює факторіал числа n рекурсивно.
    
    Аргументи:
    n -- ціле невід'ємне число
    
    Повертає:
    Факторіал числа n
    """
    if not isinstance(n, int):
        raise TypeError("Потрібно ввести ціле число.")
    if n < 0:
        raise ValueError("Факторіал не визначено для від'ємних чисел.")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
