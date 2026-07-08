# Dictionaries for number names
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
thousands = ["", "thousand", "million", "billion", "trillion"]


def number_to_words_below_1000(number: int):
    if number == 0:
        return ""
    elif number < 10:
        return ones[number]
    elif number < 20:
        return teens[number - 10]
    elif number < 100:
        return tens[number // 10] + ('' if number % 10 == 0 else '-' + ones[number % 10])
    else:
        return ones[number // 100] + ' hundred' + ('' if number % 100 == 0 else ' and ' + number_to_words_below_1000(number % 100))


def number_to_words_whole_part(number: int):
    if number == 0:
        return "zero"

    words = []
    group_index = 0

    while number > 0:
        group = number % 1000
        if group != 0:
            words.append(
                number_to_words_below_1000(group) + (' ' + thousands[group_index] if thousands[group_index] else ''))
        number //= 1000
        group_index += 1

    return ' '.join(reversed(words)).strip()


def number_to_words(number: float):
    if '.' in str(number):
        whole_part, decimal_part = str(number).split('.')
        whole_part_words = number_to_words_whole_part(int(whole_part))
        decimal_part_words = ' '.join([ones[int(digit)] for digit in decimal_part])
        if decimal_part_words:
            return f"{whole_part_words} point {decimal_part_words}"
        else:
            return f"{whole_part_words}"
    else:
        return number_to_words_whole_part(int(number))


# Test
if __name__ == '__main__':
    numbers = [0, 6, 1234, 123.45, 123., .45, 1000.89, 23467334, 1000001.01]
    for n in numbers:
        print(f"{n}\t-> {number_to_words(n)}")
