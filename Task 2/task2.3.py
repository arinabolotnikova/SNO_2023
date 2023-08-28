# Написать функцию, принимающую на вход строку из последовательности круглых, квадратных, фигурных и треугольных скобок.
# и возвращающую True если последовательность верна и False - если нет.

def check_brackets(line: str):
    ...


if __name__ == '__main__':
    # Simple tests:
    print(check_brackets('(((){[]})<>)'))  # True
    print(check_brackets('((()<{()}>)())'))  # True
    print(check_brackets('(((<){}(>)[]))'))  # False
    print(check_brackets('{<>(<[]>())}'))  # True
