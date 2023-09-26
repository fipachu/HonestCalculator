OK = 'ok'
BAD_NUMBER = 'bad_number'
BAD_OPER = 'bad_oper'
OPERATORS = '+-*/'


def take_input():
    calc = input('Enter an equation\n')
    x, oper, y = calc.split()

    try:
        float(x)
        float(y)
    except ValueError:
        print('Do you even know what numbers are? Stay focused!')
        return BAD_NUMBER

    if oper not in OPERATORS:
        # split in two lines to comply with PEP 8
        print("Yes ... an interesting math operation. "
              "You've slept through all classes, haven't you?")
        return BAD_OPER

    return OK


def ui_loop():
    while True:
        input_ = take_input()



def main():
    ui_loop()


if __name__ == "__main__":
    main()
