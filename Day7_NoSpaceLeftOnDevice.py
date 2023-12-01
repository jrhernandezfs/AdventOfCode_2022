# class FileSystemNode:
#     def __init__(self, name, size=0):
#         self.name = name
#         self.size = size
#         self.children = []
#         self.is_file = size > 0
#
#     def add_child(self, child):
#         self.children.append(child)
#
#     def calculate_total_size(self):
#         if self.is_file:
#             return self.size
#         return sum(child.calculate_total_size() for child in self.children)
#
# def parse_filesystem(input_data):
#     root = FileSystemNode("/")
#     current_dir = root
#     path = []
#
#     for line in input_data:
#         if line.startswith("$ cd"):
#             destination = line.split()[-1].strip()
#             if destination == "/":
#                 path = []
#             elif destination == "..":
#                 path.pop()
#             else:
#                 path.append(destination)
#             current_dir = root
#             for dir_name in path:
#                 found = False
#                 for child in current_dir.children:
#                     if child.name == dir_name:
#                         current_dir = child
#                         found = True
#                         break
#                 if not found:
#                     new_dir = FileSystemNode(dir_name)
#                     current_dir.add_child(new_dir)
#                     current_dir = new_dir
#         elif line.startswith("$ ls"):
#             continue
#         else:
#             parts = line.split()
#             if len(parts) == 2:
#                 size = int(parts[0]) if parts[0].isdigit() else 0
#                 name = parts[1].strip()
#                 new_node = FileSystemNode(name, size)
#                 current_dir.add_child(new_node)
#
#     return root
#
# def find_small_directories(node, max_size=100000):
#     if not node.is_file:
#         total_size = node.calculate_total_size()
#         if total_size <= max_size:
#             small_directories.append((node.name, total_size))
#         for child in node.children:
#             find_small_directories(child, max_size)
#
# # Read input from file
# with open("AC7_Input.txt", "r") as file:
#     input_data = file.readlines()
#
# # Parse the filesystem and find the small directories
# root = parse_filesystem(input_data)
# small_directories = []
# find_small_directories(root)
#
# # Calculate the sum of the total sizes of the small directories
# sum_of_small_directories = sum(size for _, size in small_directories)
# print("Small Directories:", small_directories)
# print("Sum of their total sizes:", sum_of_small_directories)
class FileSystemNode:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.children = []
        self.is_file = size > 0

    def add_child(self, child):
        self.children.append(child)

    def calculate_total_size(self):
        if self.is_file:
            return self.size
        return sum(child.calculate_total_size() for child in self.children)

def parse_filesystem(input_data):
    root = FileSystemNode("/")
    current_dir = root
    path = []

    for line in input_data:
        if line.startswith("$ cd"):
            destination = line.split()[-1].strip()
            if destination == "/":
                path = []
            elif destination == "..":
                path.pop()
            else:
                path.append(destination)
            current_dir = root
            for dir_name in path:
                found = False
                for child in current_dir.children:
                    if child.name == dir_name:
                        current_dir = child
                        found = True
                        break
                if not found:
                    new_dir = FileSystemNode(dir_name)
                    current_dir.add_child(new_dir)
                    current_dir = new_dir
        elif line.startswith("$ ls"):
            continue
        else:
            parts = line.split()
            if len(parts) == 2:
                size = int(parts[0]) if parts[0].isdigit() else 0
                name = parts[1].strip()
                new_node = FileSystemNode(name, size)
                current_dir.add_child(new_node)

    return root

def find_small_directories(node, max_size=100000):
    if not node.is_file:
        total_size = node.calculate_total_size()
        if total_size <= max_size:
            small_directories.append((node.name, total_size))
        for child in node.children:
            find_small_directories(child, max_size)

def find_smallest_eligible_directory(node, required_space):
    eligible_directories = []
    if not node.is_file:
        total_size = node.calculate_total_size()
        if total_size >= required_space:
            eligible_directories.append((node.name, total_size))
        for child in node.children:
            eligible_directories.extend(find_smallest_eligible_directory(child, required_space))
    return eligible_directories

# Read input from file
with open("AC7_Input.txt", "r") as file:
    input_data = file.readlines()

# Parse the filesystem
root = parse_filesystem(input_data)

# Part 1: Find small directories
small_directories = []
find_small_directories(root)
sum_of_small_directories = sum(size for _, size in small_directories)
print("Small Directories:", small_directories)
print("Sum of their total sizes:", sum_of_small_directories)

# Part 2: Find the smallest eligible directory for deletion
total_disk_space = 70000000
required_free_space = 30000000
used_space = root.calculate_total_size()
current_unused_space = total_disk_space - used_space
additional_space_required = required_free_space - current_unused_space
eligible_directories = find_smallest_eligible_directory(root, additional_space_required)
eligible_directories.sort(key=lambda x: x[1])
smallest_eligible_directory = eligible_directories[0] if eligible_directories else None
print("Smallest Eligible Directory for Deletion:", smallest_eligible_directory)

