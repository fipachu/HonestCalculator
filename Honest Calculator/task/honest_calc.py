# Stage 1, procedural edition.
# It seems like it works best as procedural code.
while True:
    equation = input('Enter an equation\n')
    x, oper, y = equation.split()

    try:
        float(x)
        float(y)
    except ValueError:
        print('Do you even know what numbers are? Stay focused!')
        continue

    if oper not in '+-*/':
        print("Yes ... an interesting math operation. "
              "You've slept through all classes, haven't you?")
        continue

    break
