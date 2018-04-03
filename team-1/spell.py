WORDS = [
    "", # unused
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]

TENS = [
    "",  # unused
    "",  # unused
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
    ]


def spell(value):
    if value == 0:
        return 'zero'

    remainder = value

    parts = []

    remainder = handle_scale(remainder, 1000000, "million", parts)
    remainder = handle_scale(remainder, 1000, "thousand", parts)
    remainder = handle_scale(remainder, 100, "hundred", parts)

    and_added = False

    if remainder >= 20:
        if value >= 100:
            parts.append('and')
            and_added = True
        digit = remainder // 10
        parts.append(TENS[digit])
        remainder -= digit * 10

    if remainder > 0:
        if not and_added and value >= 100:
            parts.append('and')
        parts.append(WORDS[remainder])

    return " ".join(parts)


def handle_scale(remainder, scale, name, parts):
    if remainder >= scale:
        x = remainder // scale
        parts.append(spell(x) + " " + name)
        remainder -= x * scale
    return remainder
