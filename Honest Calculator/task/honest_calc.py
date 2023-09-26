OK = 'ok'
BAD_NUMBER = 'bad_number'
BAD_OPER = 'bad_oper'
OPERATORS = '+-*/'


def process_input() -> str:
    calc = input()
    x, oper, y = calc.split()

    try:
        float(x)
        float(y)
    except ValueError:
        return BAD_NUMBER

    if oper not in OPERATORS:
        # split in two lines to comply with PEP 8
        return BAD_OPER

    return OK


def ui_loop() -> None:
    while True:
        print('Enter an equation')
        control = process_input()
        if control == BAD_NUMBER:
            print('Do you even know what numbers are? Stay focused!')
            continue
        elif control == BAD_OPER:
            print("Yes ... an interesting math operation. "
                  "You've slept through all classes, haven't you?")
            continue
        elif control == OK:
            return
        else:
            raise ValueError(f"Invalid control '{control}'")


def main():
    ui_loop()


if __name__ == "__main__":
    main()
