def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

input_numbers = input("Введите числа через пробел: ")

numbers = list(map(int, input_numbers.split()))

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Простые числа в списке:", prime_numbers)
