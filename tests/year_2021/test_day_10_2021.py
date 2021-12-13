import pytest
from adventofcode.year_2021.day_10_2021 import part_one, part_two, is_valid_chunk, get_score


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("()", ""),
        ("[]", ""),
        ("([])", ""),
        ("{()()()}", ""),
        ("<([{}])>", ""),
        ("[<>({}){}[([])<>]]", ""),
        ("(((((((((())))))))))", ""),
        ("(]", 1),
        ("{()()()>", 7),
        ("(((()))}", 7),
        ("<([]){()}[{}])", 13),
        ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
        ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
        ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
        ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
        ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
    ],
)
def test_is_valid_chunk(line, expected):
    assert expected == is_valid_chunk(line)


def test_part_one():
    assert 26397 == part_one(
        [
            "[({(<(())[]>[[{[]{<()<>>",
            "[(()[<>])]({[<{<<[]>>(",
            "{([(<{}[<>[]}>{[]{[(<()>",
            "(((({<>}<{<{<>}{[]{[]{}",
            "[[<[([]))<([[{}[[()]]]",
            "[{[{({}]{}}([{[{{{}}([]",
            "{<[[]]>}<{[{[{[]{()[[[]",
            "[<(<(<(<{}))><([]([]()",
            "<{([([[(<>()){}]>(<<{{",
            "<{([{{}}[<[[[<>{}]]]>[]]",
        ]
    )


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("}}]])})]", 288957),
        (")}>]})", 5566),
        ("}}>}>))))", 1480781),
        ("]]}}]}]}>", 995444),
        ("])}>", 294),
    ],
)
def test_get_score(line, expected):
    assert expected == get_score(line)


def test_part_two():
    assert 288957 == part_two(
        [
            "[({(<(())[]>[[{[]{<()<>>",
            "[(()[<>])]({[<{<<[]>>(",
            "{([(<{}[<>[]}>{[]{[(<()>",
            "(((({<>}<{<{<>}{[]{[]{}",
            "[[<[([]))<([[{}[[()]]]",
            "[{[{({}]{}}([{[{{{}}([]",
            "{<[[]]>}<{[{[{[]{()[[[]",
            "[<(<(<(<{}))><([]([]()",
            "<{([([[(<>()){}]>(<<{{",
            "<{([{{}}[<[[[<>{}]]]>[]]",
        ]
    )
