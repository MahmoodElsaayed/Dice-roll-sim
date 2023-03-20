from random import randint


def main():
    dice_side = dice_roller()
    print(*side_designer(dice_side), sep="\n", end="")


def dice_roller():
    return randint(1, 6)


def side_designer(number):
    n = number
    while n-2 >= 0:
        yield 2 * "🔴"
        n -= 2
    yield n * "🔴"


if __name__ == "__main__":
    main()
