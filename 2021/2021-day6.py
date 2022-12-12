import tqdm

with open("2021-day6.txt", "r", encoding="utf8") as f:
    lines: str = f.read()

ages: list[int] = [int(x) for x in lines.split(",")]

test = [3, 4, 3, 1, 2]


class Fish:
    def __init__(self, days: int = 8) -> None:
        self.days: int = days

    def live(self):
        if self.days == 0:
            self.days = 6
            return Fish()
        self.days -= 1
        return None


fish: list[Fish] = [Fish(age) for age in ages]


class School:
    def __init__(self, age_list: list) -> None:
        self.ages: dict[int, int] = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }
        for age in age_list:
            self.ages[age] += 1

    def day(self) -> None:
        self.ages = {
            0: self.ages[1],
            1: self.ages[2],
            2: self.ages[3],
            3: self.ages[4],
            4: self.ages[5],
            5: self.ages[6],
            6: self.ages[0] + self.ages[7],
            7: self.ages[8],
            8: self.ages[0],
        }


school: School = School(ages)
for _ in tqdm.tqdm(range(256)):
    school.day()


print(sum(school.ages.values()))
