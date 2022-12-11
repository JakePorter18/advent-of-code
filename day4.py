import pandas as pd

data = pd.read_csv("day4.txt", names=["a", "b"])

data["a_start"] = pd.to_numeric(data["a"].str.split("-", expand=True)[0])
data["a_end"] = pd.to_numeric(data["a"].str.split("-", expand=True)[1])
data["a_list"] = data.apply(lambda x: list(range(x.a_start, x.a_end + 1)), axis=1)

data["b_start"] = pd.to_numeric(data["b"].str.split("-", expand=True)[0])
data["b_end"] = pd.to_numeric(data["b"].str.split("-", expand=True)[1])
data["b_list"] = data.apply(lambda x: list(range(x.b_start, x.b_end + 1)), axis=1)


def is_contained(a_start: int, a_end: int, b_start: int, b_end: int) -> int:
    if ((a_start <= b_start) and (a_end >= b_end)) or (
        (a_start >= b_start) and (a_end <= b_end)
    ):
        return 1
    else:
        return 0


def is_intersect(a_list: list[int], b_list: list[int]) -> int:
    return 1 if set(a_list).intersection(b_list) else 0


data["contained"] = data.apply(
    lambda x: is_contained(x.a_start, x.a_end, x.b_start, x.b_end), axis=1
)
data["intersect"] = data.apply(
    lambda x: is_intersect(
        x.a_list,
        x.b_list,
    ),
    axis=1,
)


print(data.sum())
