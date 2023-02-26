### Exercise - 19 - Resistor Colour Duo
def value(colors):
    codes = {'black': 0,
              'brown': 1,
              'red': 2,
              'orange': 3,
              'yellow': 4,
              'green': 5,
              'blue': 6,
              'violet': 7,
              'grey': 8,
              'white': 9}

    resistance = []
    for i in colors[0:2]:
        resistance.append(str(codes[i]))
    return int(''.join(resistance))