def is_palindrome_recursive(s):
    """
    Перевіряє, чи є рядок паліндромом рекурсивно.
    
    Аргументи:
    s -- рядок
    
    Повертає:
    True, якщо рядок є паліндромом, інакше False
    """
    if not isinstance(s, str):
        raise TypeError("Потрібно ввести рядок.")
    
    # Приберемо пробіли і приведемо до нижнього регістру
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])
