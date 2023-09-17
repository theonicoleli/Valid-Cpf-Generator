import re

def get_digit(pedido: str) -> int:
    len_pedido = len(pedido) + 1

    multiplication = []
    for pedido_index, multiplier in enumerate(range(len_pedido, 1, -1)):
        multiplication.append(int(pedido[pedido_index]) * multiplier)
    total_sum = sum(multiplication)
    digit = 11 - (total_sum % 11)
    return digit if digit < 10 else 0

def get_digit_one(pedido: str) -> int:
    return get_digit(pedido[:9])

def get_digit_two(pedido: str) -> int:
    return get_digit(pedido[:10])

def remove_not_number(pedido: str) -> str:
    return re.sub(r'\D', '', pedido)

def has_eleven_chars(value: str) -> bool:
    return len(value) == 11

def is_sequence(value: str) -> bool:
    return (value[0] * len(value)) == value

def is_valid(pedido: str) -> bool:
    clean_pedido = remove_not_number(pedido)

    if not has_eleven_chars(clean_pedido):
        return False

    if is_sequence(clean_pedido):
        return False

    digit_one = get_digit_one(clean_pedido)
    digit_two = get_digit_two(clean_pedido)

    new_pedido = f'{clean_pedido[:9]}{digit_one}{digit_two}'

    return new_pedido == clean_pedido

if __name__ == "__main__":
    while True:
        pedido = input('Digite o CPF para verificar se é válido: ')
        if is_valid(pedido):
            print('Seu CPF é válido!')
        else:
            print('Seu CPF não é válido!')