import re
from typing import Optional


class File:
    name: str
    size: int

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __repr__(self) -> str:
        return f"{self.name} (size={self.size})"


class Dir:
    name: str
    parent: "Dir"
    children: list["Dir"]
    files: list[File]
    total_size: int

    def __init__(
        self,
        name: str,
        parent: "Dir" = None,
        children: list["Dir"] = None,
        files: list[File] = None,
    ) -> None:
        self.name = name
        self.parent = parent
        self.children = children if children else []
        self.files = files if files else []
        self.total_size = 0

    def __repr__(self) -> str:
        return f"{self.name} (size={self.total_size})"

    def calculate_total_size(self):
        self.total_size = 0
        for file in self.files:
            self.total_size += file.size

        for child in self.children:
            child.calculate_total_size()
            self.total_size += child.total_size


current_dir: Optional[Dir] = None


def is_command(cmd: str) -> bool:
    return cmd.startswith("$")


def handle_cd(cmd: str):
    folder_name = re.findall(r"[\w/\.]+$", cmd).pop()

    global current_dir
    if folder_name == "..":
        current_dir = current_dir.parent
    elif current_dir is None:
        current_dir = Dir(folder_name)
    else:
        new_dir = Dir(folder_name, current_dir)
        current_dir.children.append(new_dir)
        current_dir = new_dir


def handle_ls(cmd: str):
    global current_dir
    if not cmd.startswith("dir"):
        size, filename = cmd.split()
        f = File(filename, int(size))
        current_dir.files.append(f)
        current_dir.calculate_total_size()


def parse_command(cmd: str):
    if "cd" in cmd:
        handle_cd(cmd)


def goto_root(current_dir: Dir) -> Dir:
    while current_dir.parent:
        current_dir = current_dir.parent
    return current_dir


def find_dirs_to_delete(
    dir: Dir, space_to_be_cleared: int, sizes: list[int]
) -> list[int]:
    if dir.total_size >= space_to_be_cleared:
        sizes.append(dir.total_size)

    for child in dir.children:
        find_dirs_to_delete(child, space_to_be_cleared, sizes)

    return sizes


while True:
    try:
        cmd = input()

        if is_command(cmd):
            parse_command(cmd)
            continue

        handle_ls(cmd)
    except EOFError:
        break


current_dir = goto_root(current_dir)
current_dir.calculate_total_size()


total_space = 70000000
space_required = 30000000

space_to_be_cleared = space_required - (total_space - current_dir.total_size)

print(min(find_dirs_to_delete(current_dir, space_to_be_cleared, [])))
