from typing import List

from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


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
            if is_abba_sequence(ip[i: i + 4]):
                if inside_brackets:
                    return False
                abba_count += 1
    return abba_count > 0


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
                bab_sequences.append(sequence[i: i + 3])
            else:
                aba_sequences.append(sequence[i: i + 3])
    return aba_sequences, bab_sequences


def does_support_ssl(ip):
    aba_sequences, bab_sequences = get_aba_sequences(ip)
    for aba in aba_sequences:
        for bab in bab_sequences:
            if aba[0] == bab[1] and aba[1] == bab[0]:
                return True
    return False


@solution_timer(2016, 7, 1)
def part_one(input_data: List[str]):
    tls_count = 0
    for ip in input_data:
        if does_support_tls(ip):
            tls_count += 1
    return tls_count


@solution_timer(2016, 7, 2)
def part_two(input_data: List[str]):
    ssl_count = 0
    for ip in input_data:
        if does_support_ssl(ip):
            ssl_count += 1
    return ssl_count


if __name__ == "__main__":
    data = get_input_for_day(2016, 7)
    part_one(data)
    part_two(data)
