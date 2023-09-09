from aocd import data, submit

data = data.split("\n")
shape_score_lookup = {"X": 1, "Y": 2, "Z": 3, "A": 0, "B": 1, "C": 2}


def score(round_str: str) -> int:
    my_shape_score = shape_score_lookup[round_str[-1]]
    opponent_shape_score = shape_score_lookup[round_str[0]]
    return my_shape_score + 3 * ((my_shape_score - opponent_shape_score) % 3)


my_total_score = sum(list(map(score, data)))
# submit(my_total_score, part="a", day=2, year=2022)

strategy_outcome_score_lookup = {"X": 0, "Y": 1, "Z": 2}


def score_new(round_str: str) -> int:
    outcome_code = strategy_outcome_score_lookup[round_str[-1]]
    outcome_score = 3 * outcome_code
    my_shape_score = (outcome_code + shape_score_lookup[round_str[0]]) % 3
    if my_shape_score == 0:
        my_shape_score = 3
    return outcome_score + my_shape_score


my_total_score_new = sum(list(map(score_new, data)))
# submit(my_total_score_new, part="b", day=1, year=2022)
