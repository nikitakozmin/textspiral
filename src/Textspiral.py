import itertools
import time


def textspiral(text, size_x=3, size_y=3, isprint=True):
    text = itertools.cycle(text)
    field = [["*"]*size_x for _ in range(size_y)]
    print_field(field)
    x, y = -1, 0
    add_x, add_y = 1, 0
    time_costs = 5
    delay = time_costs / (size_x * size_y)
    while True:
        if ((-1 < x + add_x < size_x) and (-1 < y + add_y < size_y)) and field[y + add_y][x + add_x] == "*":
            x += add_x
            y += + add_y
            field[y][x] = next(text)
            if isprint:
                print_field(field)
                time.sleep(delay)
        else:
            add_x, add_y = -add_y, add_x
            if field[y + add_y][x + add_x] != "*":
                break
    return field


clear_display = lambda: print("\033c\033[3J", end='')

def print_field(field):
    clear_display()
    for a in field:
        print(*a)


if __name__ == "__main__":
    textspiral(input("Input text: "), 
               int(input("Input length: ")), 
               int(input("Input height: ")))
