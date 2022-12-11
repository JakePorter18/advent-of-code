from typing import Optional

with open("day7.txt", "r", encoding="utf8") as f:
    lines: list[str] = [line.rstrip("\n") for line in f]


class File:
    def __init__(self, data: str, path: list[str]) -> None:
        self.path: list[str] = list(path)
        size: str
        self.name: str
        size, self.name = data.split(" ")
        self.size: int = int(size)

    def __str__(self) -> str:
        return "/".join(self.path) + "/" + self.name + f" ({self.size})"


class Directory:
    def __init__(
        self, data: Optional[str] = None, path: Optional[list[str]] = None
    ) -> None:
        self.path: list[str] = list(path)  # type: ignore
        if data is not None:
            self.path.append(data)
            self.name: str = data
        else:
            self.name = "/"
        self.size: int = 0

    def __str__(self) -> str:
        return "/".join(self.path) + f" ({self.size})"


path: list[str] = ["/"]
directories: list[Directory] = [Directory(None, path)]
files: list[File] = []
for line in lines:
    if line[0] == "$":
        if line == "$ cd /":
            path = ["/"]

        elif line == "$ cd ..":
            path.pop(-1)

        elif line[:5] == "$ cd ":
            path.append(line[6:])

    elif line[:3] == "dir":
        directories.append(Directory(line[5:], path))
    else:
        files.append(File(line, path))

# print(len(files))
# print(directories)
# print(path)


def is_in_directory(file_path: list[str], directory_path: list[str]) -> bool:
    try:
        return all(
            directory_path[x] == file_path[x] for x in range(len(directory_path))
        )
    except IndexError:
        return False


for directory in directories:
    for file in files:
        if is_in_directory(file.path, directory.path):
            directory.size += file.size


def myFunc(e) -> int:
    return e.size


significant: list[Directory] = []
directories.sort(key=myFunc, reverse=True)

print("Part 1")
print(sum(dir.size for dir in directories if dir.size <= 100_000))

total_space: int = 70_000_000
used: int = directories[0].size
empty: int = total_space - used
required: int = 30_000_000 - empty


print("Part 1")
print(min(dir.size for dir in directories if dir.size >= required))
