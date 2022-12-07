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


def get_dir_to_sum(dir: Dir, sizes: list[int]):
    if dir.total_size < 100000:
        sizes.append(dir.total_size)

    for child in dir.children:
        get_dir_to_sum(child, sizes)

    return sizes


# Uncomment the code below to print the filesystem
# def print_dirs(dir: Dir, pad: int = 0, old_pad: int = 0, last_child: bool = False):
#     if dir.parent is None:
#         print(f"dir {dir.name} (size={dir.total_size})")
#     else:
#         print(
#             f"{'│' if old_pad != 0 else ''}{old_pad * ' '}{'├' if not last_child else '└'}{2 * '─'} dir {dir.name} (size={dir.total_size})"
#         )

#     for i, file in enumerate(dir.files):
#         if i + 1 == len(dir.files) and not dir.children:
#             print(
#                 f"{'│' if dir.parent is not None else ''}{pad * ' '}└{2 * '─'} {file.name} (file, size={file.size})"
#             )
#             continue

#         print(
#             f"{'│' if dir.parent is not None else ''}{pad * ' '}├{2 * '─'} {file.name} (file, size={file.size})"
#         )

#     for i, child in enumerate(dir.children):
#         if i + 1 == len(dir.children):
#             print_dirs(child, pad + 4, pad, True)
#             continue
#         print_dirs(child, pad + 4, pad)


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


print(sum(get_dir_to_sum(current_dir, [])))
