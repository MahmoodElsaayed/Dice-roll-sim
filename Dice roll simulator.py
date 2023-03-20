from random import randint


def main():
    face_number = dice_roller()
    print(*dice_designer(face_number), sep="\n", end="")


def dice_roller():
    return randint(1, 6)


def dice_designer(number):
    n = number
    while n-2 >= 0:
        yield 2 * "🔴"
        n -= 2
    yield n * "🔴"


if __name__ == "__main__":
    main()
