import random

def generate_lotto_numbers_6_42():
    lotto_numbers = random.sample(range(1, 43), 6)
    lotto_numbers.sort()
    return lotto_numbers

def generate_lotto_numbers_6_55():
    lotto_numbers = random.sample(range(1, 56), 6)
    lotto_numbers.sort()
    return lotto_numbers

def format_numbers(numbers):
    
    return [f"{num:2d}" for num in numbers]


lotto_numbers_6_42 = generate_lotto_numbers_6_42()
formatted_6_42 = format_numbers(lotto_numbers_6_42)
print("Your PCSO 6/42 Lotto numbers are:", formatted_6_42)


lotto_numbers_6_55 = generate_lotto_numbers_6_55()
formatted_6_55 = format_numbers(lotto_numbers_6_55)
print("Your PCSO 6/55 Lotto numbers are:", formatted_6_55)
