#!/usr/local/bin/python3

start = 145852
end = 616942
input = [x for x in range(start, end)]


def has_two_equal_adjacent_digits(number):
    l = [x for x in str(number)]
    n = 1
    for c in range(0, len(l)-1):
        if l[c] == l[c + 1]:
            n += 1
        else:
            if n == 2:
                return True

            n = 1

    return n == 2


def never_decreases(number):
    l = [x for x in str(number)]
    return l == sorted(l)


def is_valid_password(number):
    if has_two_equal_adjacent_digits(number) and never_decreases(number):
        return True

    return False


if __name__ == "__main__":
    potential_passwords = map(is_valid_password, input)
    valid_passwords = [x for x in potential_passwords if x == True]

    print("In this range, there are {} valid passwords").format(
        len(valid_passwords))
