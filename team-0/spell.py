def main():
    try:
        num = input("What's your number")
        num = int(num)
    except ValueError:
        print("That's not a number")
        exit()

    if num >= 1000000000:
        print("That's too large")
        exit()

    printnumber(num)

digits = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
weirds = {
    10: "ten",
    11: "eleven",
    12: "twelve",
}
tens = {
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

# TODO
bignumberblocks = {
    1: 'thousand',
    2: 'million',
    #3: 'billions',
    #4: 'trillions',
}


def printnumber(num):
    numstring = str(num)

    # TODO
    if len(numstring) > 6:
        threedigitblock(int(numstring[0:-6]))
        print(" million ", end='')
        num = num % 10**6
        numstring = str(num)

    if len(numstring) > 3:
        threedigitblock(int(numstring[0:-3]))
        print(" thousand ", end='')
        num = num % 10**3
        numstring = str(num)

    if num == 0:
        return

    threedigitblock(int(numstring))


def threedigitblock(num):
    numstring = str(num)
    if num >= 100:
        print( "%s %s" % (digits[int(numstring[0])], "hundred"), end='')
        if num % 100 == 0:
                return
        print(" and ", end='')
        num = num % 100

    if num < 10:
        print(digits[num], end='')
        return
    if num < 13:
        print(weirds[num], end='')
        return
    if num < 20:
        print(tens[ int( numstring[-1] ) ][0:-1] + "een", end='')
        return

    if num % 10 == 0:
        print(tens[ int(numstring[-2]) ], end='')
        return
    else:
        print( "%s %s" % (tens[ int(numstring[-2]) ], digits[ int(numstring[-1]) ]) , end='')


if __name__ == "__main__":
    main()
