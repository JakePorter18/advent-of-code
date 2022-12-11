from typing import Union


with open("day6.txt", "r", encoding="utf8") as f:
    lines: str = f.read()

# print(lines)


def get_location(
    input_string: str, window_length: int = 14
) -> dict[str, Union[str, int]]:
    start: int = 0
    input_length: int = len(input_string)

    while True:
        end: int = start + window_length
        if end > input_length:
            raise IndexError(f"No location found for {window_length=}")
        window: str = input_string[start:end]
        letters: set[str] = set(list(window))
        if len(letters) == window_length:
            break
        else:
            start += 1

    return {"start": start, "end": end, "text": window}


for x in range(len(lines)):
    print(x, get_location(lines, x))
