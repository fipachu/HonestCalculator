ALLOWED_OPERATORS = '+-*/'


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
    # # Alternatively, against the spirit of the exercise:
    # for op in ALLOWED_OPERATORS:
    #     if op == oper:
    #         return eval(f'{x}{op}{y}')
    # else:
    #     raise ValueError(f"Wrong operator! '{oper}' "
    #                      f"not in '{ALLOWED_OPERATORS}'")
    # # I wonder if there is a way to allow for using
    # # user defined lists of operators without using eval()


def ui_loop() -> None:
    while True:
        equation = input('Enter an equation\n')
        x, oper, y = equation.split()

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
        return


def main():
    ui_loop()


if __name__ == "__main__":
    main()


# Nothing interesting here, move on.
def evil_hack():
    while True:
        equation = input('Enter an equation\n')
        try:
            print(eval(equation))
            return
        except NameError:
            print('Do you even know what numbers are? Stay focused!')
            continue
        except SyntaxError:
            print("Yes ... an interesting math operation. "
                  "You've slept through all classes, haven't you?")
            continue
        except ZeroDivisionError:
            print('Yeah... division by zero. Smart move...')
            continue
    # Seriously though, they thought of it. The unit test knows
    # if you used eval() in your solution.
