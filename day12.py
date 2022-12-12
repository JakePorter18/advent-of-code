import re
from tqdm import tqdm
import math


with open("day12.txt", "r", encoding="utf8") as f:
    lines: list[str] = [line.rstrip("\n") for line in f]
