# Advent of code Year 2016 Day 7 solution
# Author = Frazzer951
# Date = November 2021

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read().split("\n")


def is_abba_sequence(sequence):
    for i in range(len(sequence) - 3):
        if (
            sequence[i] == sequence[i + 3]
            and sequence[i + 1] == sequence[i + 2]
            and sequence[i] != sequence[i + 1]
        ):
            return True
    return False


def does_support_tls(ip):
    abba_count = 0
    inside_brackets = False
    for i in range(len(ip)):
        if ip[i] == "[":
            inside_brackets = True
        elif ip[i] == "]":
            inside_brackets = False
        else:
            if is_abba_sequence(ip[i : i + 4]):
                if inside_brackets:
                    return False
                abba_count += 1
    return abba_count > 0


def part1(input):
    tls_count = 0
    for ip in input:
        if does_support_tls(ip):
            tls_count += 1
    return tls_count


assert does_support_tls("abba[mnop]qrst") == True
assert does_support_tls("abcd[bddb]xyyx") == False
assert does_support_tls("aaaa[qwer]tyui") == False
assert does_support_tls("ioxxoj[asdfgh]zxcvbn") == True

p1 = part1(input)
print("Part One : " + str(p1))


def get_aba_sequences(sequence):
    aba_sequences = []
    bab_sequences = []
    inside_brackets = False
    for i in range(len(sequence) - 2):
        if sequence[i] == "[" or sequence[i + 1] == "[" or sequence[i + 2] == "[":
            inside_brackets = True
            continue
        if sequence[i] == "]" or sequence[i + 1] == "]" or sequence[i + 2] == "]":
            inside_brackets = False
            continue
        if sequence[i] == sequence[i + 2] and sequence[i] != sequence[i + 1]:
            if inside_brackets:
                bab_sequences.append(sequence[i : i + 3])
            else:
                aba_sequences.append(sequence[i : i + 3])
    return aba_sequences, bab_sequences


def does_support_ssl(ip):
    aba_sequences, bab_sequences = get_aba_sequences(ip)
    for aba in aba_sequences:
        for bab in bab_sequences:
            if aba[0] == bab[1] and aba[1] == bab[0]:
                return True
    return False


def part2(input):
    ssl_count = 0
    for ip in input:
        if does_support_ssl(ip):
            ssl_count += 1
    return ssl_count


assert does_support_ssl("aba[bab]xyz") == True
assert does_support_ssl("xyx[xyx]xyx") == False
assert does_support_ssl("aaa[kek]eke") == True
assert does_support_ssl("zazbz[bzb]cdb") == True

p2 = part2(input)
print("Part Two : " + str(p2))
