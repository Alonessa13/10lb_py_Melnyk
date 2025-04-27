from factorial_recursive import factorial_recursive
from fibonacci_recursive import fibonacci_recursive
from sum_list_recursive import sum_list_recursive
from is_palindrome_recursive import is_palindrome_recursive

def main():
    # Тестуємо функцію факторіала
    print("Факторіал 5:", factorial_recursive(5))
    
    # Тестуємо функцію Фібоначчі
    print("7-ме число Фібоначчі:", fibonacci_recursive(7))
    
    # Тестуємо функцію суми списку
    numbers = [1, 2, 3, 4, 5]
    print("Сума елементів списку", numbers, ":", sum_list_recursive(numbers))
    
    # Тестуємо функцію перевірки паліндрома
    word = "A man a plan a canal Panama"
    print(f"'{word}' є паліндромом?", is_palindrome_recursive(word))

if __name__ == "__main__":
    main()
