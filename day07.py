# from aocd import data
import re


class Directory:
    def __init__(self, name, parent, children, size) -> None:
        self.name = name
        self.parent = parent
        self.children = children
        self.size = size


root = None
curr_dir = None

with open("input.txt") as f:
    while True:
        line = f.readline().strip("\n")
        if not line:
            break

        line_segs = line.split(" ")
        if line_segs[0] == "$":
            if len(line_segs) == 3:
                curr_name = line_segs[-1]
                if curr_name == "/":
                    root = Directory(curr_name, None, {}, 0)
                    curr_dir = root
                elif curr_name == "..":
                    if len(curr_dir.children) > 0:
                        curr_dir.size += sum(
                            [d.size for d in curr_dir.children.values()]
                        )
                    curr_dir = curr_dir.parent
                else:
                    curr_dir = curr_dir.children[curr_name]

        if line_segs[0] == "dir":
            dir_name = line_segs[1]
            curr_dir.children[dir_name] = Directory(dir_name, curr_dir, {}, 0)

        if line_segs[0].isnumeric():
            curr_dir.size += int(line_segs[0])

root.size += sum([d.size for d in root.children.values()])

# We have constructed the tree. Now on to question #1:


def get_small_dirs_total_size(node: Directory, threshold=100_000) -> list():
    res = 0
    if node.size <= threshold:
        res += node.size
    for child_node in node.children.values():
        res += get_small_dirs_total_size(child_node, threshold)
    return res


answer_a = get_small_dirs_total_size(root, 100_000)
print(f"{answer_a = }")

disk_size = 70_000_000
free_space = disk_size - root.size
required_space = 30_000_000


def find_smallest_dir_to_del(
    node: Directory, space_to_reclaim: int, curr_candidate=None
) -> Directory:
    if node.size >= space_to_reclaim:
        if curr_candidate is None:
            curr_candidate = node
        else:
            if node.size < curr_candidate.size:
                curr_candidate = node

    for child_node in node.children.values():
        smallest_child = find_smallest_dir_to_del(
            child_node, space_to_reclaim, curr_candidate
        )
        if (
            smallest_child.size < curr_candidate.size
            and smallest_child.size >= space_to_reclaim
        ):
            curr_candidate = smallest_child

    return curr_candidate


answer_b = find_smallest_dir_to_del(root, required_space - free_space).size
print(f"{answer_b = }")
