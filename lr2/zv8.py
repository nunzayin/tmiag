#!/usr/bin/env python3

from random import randint

ANSWER_YES_ALIAS = ("yes", "y", "да", "д")
ANSWER_NO_ALIAS = ("no", "n", "нет", "не", "н")
RAND_ELEMS_RANGE = (-100, 100)
RAND_GEN_TIMES = 10

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
    res = {}
    print("Вводите целые числа через пробел или Enter (можно совмещать).")
    print("Введите \"!\", чтобы завершить ввод.")
    while True:
        usr_input = input("> ")
        if usr_input == "!":
            break
        try:
            res |= set(map(int, usr_input.split()))
        except Exception as e:
            print("Ошибка ввода: {e}")
    return res

def main():
    A = {}
    if ask("Сгенерировать значения автоматически?"):
        A = generate_set()
    else:
        A = input_set()
    print(A)

if __name__ == "__main__":
    main()
