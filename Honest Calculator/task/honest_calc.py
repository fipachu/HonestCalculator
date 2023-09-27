ALLOWED_OPERATORS = '+-*/'
M = 'M'
Y, N = 'y', 'n'


def is_allowed(oper: str) -> bool:
    """Return True if s is one of the allowed operators."""
    if len(oper) != 1:
        raise ValueError('Bad operator. It has to be ONE of the '
                         f'following math operators: {ALLOWED_OPERATORS}')

    if oper in ALLOWED_OPERATORS:
        return True
    else:
        return False


def is_number(s: str) -> bool:
    """Return True if s can be cast to float.

    If not, return False.
    """
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


def calculate(x: float, y: float, oper: str) -> float:
    """Return result of equation 'x oper y'.

    If oper is not a valid operator, raise ValueError
    """
    match oper:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y
        case _:
            raise ValueError(f"Wrong operator! '{oper}' "
                             f"not in '{ALLOWED_OPERATORS}'")


def keep_going() -> bool:
    """Return True if user wants to keep using the calculator.

    If not, return False.
    """
    while True:
        answer = input('Do you want to continue calculations? (y / n):\n')
        if answer == Y:
            return True
        elif answer == N:
            return False
        else:
            continue


def remember() -> bool:
    """Return True if user wants to store the result.

    If not, return False.
    """
    while True:
        answer = input('Do you want to store the result? (y / n):\n')
        if answer == Y:
            return True
        elif answer == N:
            return False
        else:
            continue


def is_one_digit(x) -> bool:
    """Return True if x is a one digit int, or False if it isn't.
    """
    if -10 < x < 10 and x.is_integer():
        return True
    else:
        return False


def check(x, y, oper):
    """Check if the user is a lazy little sloth."""
    msg = ''

    if is_one_digit(x) and is_one_digit(y):
        msg += ' ... lazy'
    if x == 1 or y == 1:
        msg += ' ... very lazy'
    if (x == 0 or y == 0) and oper in '*+-':
        msg += ' ... very, very lazy'

    if msg:
        print(f'You are{msg}')


def calculator() -> None:
    """Run a sassy, if extremely rudimentary calculator."""
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

        check(x, y, oper)

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
