#input = open(r"Day7\\test_day7.txt", "r")
input = open(r"Day7\\input_day7.txt", "r")
input = input.read().split('\n')
#input = [x.split(',') for x in input]

# A file gets represented as this class.
class File:
    name: str = ''
    size: int = 0
    parent = None

    def __init__(self, name: str, size: int, parent):
        self.name = name
        self.size = int(size)
        self.parent = parent
    
    def get_size(self, collection):
        return self.size, collection
    
    def get_parent(self):
        return self.parent
    
    def print_self(self, indent: int):
        line = '  '*indent
        line += ' -'
        line += f' {self.name}'
        line += f' (file, size={self.size})'
        print(line)

# A folder gets represented as this class. This seems more sensible because of get_size() recursion and custom methods.
class Folder:
    name: str = ''
    children: list = None
    parent = None

    def __init__(self, name: str, parent):
        self.name = name
        self.children = []
        self.parent = parent

    def add_child(self, newChild):
        flag = False
        for child in self.children:
            if child.name == newChild.name:
                flag = True
        if not flag:
            self.children.append(newChild)

    def get_child(self, name: str):
        for child in self.children:
            if child.name == name and type(child) == Folder:
                return child
        return None
    
    def get_size(self, collection: list):
        total_size = 0
        for child in self.children:
            childs_size, _nill = child.get_size(collection)
            total_size += childs_size
            if type(child) == Folder:
                collection.append(childs_size)
                #collection[child.name] = childs_size


        return total_size, collection

    def get_parent(self):
        return self.parent

    def print_self(self, indent: int):
        line = '  '*indent
        line += ' -'
        line += f' {self.name}'
        line += f' (dir)'
        print(line)
        new_indent = indent + 2
        if len(self.children) > 0:
            for child in self.children:
                child.print_self(new_indent)

def navigate(name: str, cur_dir: Folder):
    next_dir = cur_dir.get_child(name)
    # create directory if not existent yet
    if not next_dir:
        next_dir = cur_dir.add_child(Folder(name))
    return next_dir

# weird pointer that shows where in the FS we currently are


root_dir: Folder = Folder('/', None)
pointer: Folder = root_dir


for line in input:
    # Command
    if line == '':
        continue
    if line.startswith('$ '):
        line = line.replace('$ ', '')
        line = line.split(' ')
        if line[0] == 'cd':
            if line[1] == '/':
                pointer = root_dir
            elif line[1] == '..':
                pointer = pointer.get_parent()
                if not pointer:
                    print('You can\'t cd .. in the root dir. That\'s illegal.')
            else:
                pointer = navigate(line[1], pointer)
        elif line[0] == 'ls':
            # Prepare for input?
            pass
    
    # Command Output
    else:
        line = line.split(' ')
        if line[0] == 'dir':
            newChild: Folder = Folder(line[1], pointer)
        else:
            # line[0] = size, line[1] = name
            newChild: File = File(line[1], line[0], pointer)
        for child in pointer.children:
            pass
        pointer.add_child(newChild)
        for child in pointer.children:
            pass


def print_tree(root: Folder, indent: int):
    root.print_self(indent)

#print_tree(root_dir, 0)
collection: list = []
root_size, collection = root_dir.get_size(collection)
collection.append(root_size)
#print(f'Size of Folder /: {root_size}')


total_size = 0
print(collection)
for size in collection:
    if size <= 100000:
        total_size += size
        #print(f"{size}")

print("Solution Part 1:")
print(f"The sum of the total sizes of those directories of at most 100000 is {total_size}")
print("Solution Part 2:")
print(f"")
