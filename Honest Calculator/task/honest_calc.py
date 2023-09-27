ALLOWED_OPERATORS = '+-*/'
M = 'M'
Y, N = 'y', 'n'


def is_allowed(s: str) -> bool:
    if s in ALLOWED_OPERATORS:
        return True
    else:
        return False


def is_number(s: str) -> bool:
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


def calculate(x: float, y: float, oper: str) -> float:
    match oper:
        case '+':
            return x+y
        case '-':
            return x-y
        case '*':
            return x*y
        case '/':
            return x/y
        case _:
            raise ValueError(f"Wrong operator! '{oper}' "
                             f"not in '{ALLOWED_OPERATORS}'")


def keep_going() -> bool:
    while True:
        answer = input('Do you want to continue calculations? (y / n):\n')
        if answer == Y:
            return True
        elif answer == N:
            return False
        else:
            continue


def remember() -> bool:
    while True:
        answer = input('Do you want to store the result? (y / n):\n')
        if answer == Y:
            return True
        elif answer == N:
            return False
        else:
            continue


def calculator() -> None:
    memory: float = 0.0  # Apparently it has to be a float.
    while True:
        equation = input('Enter an equation\n')
        x, oper, y = equation.split()

        if x == M:
            x = memory
        if y == M:
            y = memory

        if is_number(x) and is_number(y):
            x, y = float(x), float(y)
        else:
            print('Do you even know what numbers are? Stay focused!')
            continue

        if not is_allowed(oper):
            print("Yes ... an interesting math operation. "
                  "You've slept through all classes, haven't you?")
            continue

        try:
            result = calculate(x, y, oper)
        except ZeroDivisionError:
            print('Yeah... division by zero. Smart move...')
            continue
        print(result)

        if remember():
            memory = result

        if keep_going():
            continue
        else:
            return


def main():
    calculator()


if __name__ == "__main__":
    main()
