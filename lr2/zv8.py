#!/usr/bin/env python3

from random import randint

ANSWER_YES_ALIAS = ("yes", "y", "да", "д")
ANSWER_NO_ALIAS = ("no", "n", "нет", "не", "н")
RAND_ELEMS_RANGE = (-100, 100)
RAND_GEN_TIMES = 5
PREDICATE = lambda a, b: not a % b == 0
CONSOLE_COLOR_GREEN = "\x1b[1;32;40m"
CONSOLE_COLOR_RED = "\x1b[1;31;40m"
CONSOLE_COLOR_RESET = "\x1b[0m"
USE_COLORS = True

def ask(prompt, isYesDefault=True):
    while True:
        ask_suffix = "[Y/n]" if isYesDefault else "[y/N]"
        usr_input = input(f"{prompt} {ask_suffix}: ")
        if isYesDefault:
            if (usr_input == "") or (usr_input in ANSWER_YES_ALIAS):
                return True
            elif usr_input in ANSWER_NO_ALIAS:
                return False
        else:
            if usr_input in ANSWER_YES_ALIAS:
                return True
            elif (usr_input == "") or (usr_input in ANSWER_NO_ALIAS):
                return False

def generate_set():
    return {randint(*RAND_ELEMS_RANGE) for i in range(RAND_GEN_TIMES)}

def input_set():
    res = set()
    print("Вводите целые числа через пробел или Enter (можно совмещать).")
    print("Введите \"!\", чтобы завершить ввод.")
    while True:
        usr_input = input("> ")
        if usr_input == "!":
            break
        try:
            res |= set(map(int, usr_input.split()))
        except Exception as e:
            print(f"Ошибка ввода: {e}")
    return res

def descartes_sqr(s):
    return [[(s[i], s[j]) for j in range(len(s))] for i in range(len(s))]

def predicate_sqr(s, P):
    return [[P(*s[i][j]) for j in range(len(s))] for i in range(len(s))]

def print_square(s, ps):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if USE_COLORS:
                print(
                    "| {}{:4d},{:4d}{} ".format(
                        CONSOLE_COLOR_GREEN if ps[i][j] else CONSOLE_COLOR_RED,
                        s[i][j][0],
                        s[i][j][1],
                        CONSOLE_COLOR_RESET),
                    end = "")
            else:
                print(
                    "| {:4d},{:4d} [{}] ".format(
                        s[i][j][0],
                        s[i][j][1],
                        "T" if ps[i][j] else "F"),
                    end = "")
        print("|")

def main():
    A = set()

    if ask("Сгенерировать значения автоматически?"):
        A = generate_set()
    else:
        A = input_set()

    print(f"Исходное мн-во:\n{A}")

    A_sqr = descartes_sqr(list(A))
    P_sqr = predicate_sqr(A_sqr, PREDICATE)

    print("Декартов квадрат{}:".format(
        " (T - составляет отношение, F - не составляет)" if not USE_COLORS else ""
        ))
    print_square(A_sqr, P_sqr)

if __name__ == "__main__":
    main()
