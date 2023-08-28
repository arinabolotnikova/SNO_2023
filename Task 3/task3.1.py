# Написать функцию, которая на вход принимает строку в формате FEN - шахматную позицию.
# На доске находятся ладьи. Функция должна возвращать False, если хотя бы одна ладья атакует другую и True - если нет.

def check_rooks(line: str):
    ...


if __name__ == '__main__':
    # Simple tests:
    print(check_rooks('7R/5R2/6R1/1R6/4R3/2R5/3R4/R7'))  # True
    print(check_rooks('7R/2R5/5RR1/1R6/3R2R1/3R3R/2R5/R7'))  # False
    print(check_rooks('8/8/8/8/8/8/8/8'))  # True
    print(check_rooks('8/8/8/8/8/8/8/R7'))  # True