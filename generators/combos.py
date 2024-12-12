from pprint import pprint
FOX = """
U-Air
D-Air
Falling-D-Air
B-Air
F-Air
N-Air

U-Tilt
D-Tilt
F-Tilt
Jab

Up-B
Side-B
Down-B
Neutral-B

F-Smash
D-Smash
U-Smash

Grab
F-Throw
U-Throw
B-Throw
D-Throw

Grab F-Throw
Grab U-Throw
Grab B-Throw
Grab D-Throw



U-Air U-Air
U-Air D-Air
U-Air F-Air
U-Air N-Air
U-Air F-Smash

Falling-D-Air Grab
Falling-D-Air D-Air

B-Air D-Air
B-Air F-Air

F-Air F-Air
F-Air N-Air
F-Air D-Air
F-Air U-Tilt
F-Air Up-B
F-Air F-Smash
F-Air D-Smash
F-Air Grab
F-Air Neutral-B

N-Air F-Air
N-Air D-Air
N-Air F-Smash
N-Air Up-B

U-Tilt D-Air
U-Tilt N-Air
U-Tilt B-Air
U-Tilt F-Air
U-Tilt U-Air
U-Tilt U-Air
U-Tilt F-Smash

D-Tilt Grab _

F-Throw Grab _
F-Throw F-Smash _
F-Throw F-Tilt
F-Throw D-Smash *

U-Throw Grab
U-Throw F-Air
U-Throw N-Air
U-Throw D-Air
U-Throw B-Air
U-Throw U-Air
U-Throw F-Smash
"""
data=FOX

text = data.strip().replace(" ", " ")

graph = {}

for line in text.split("\n"):
    line = line.strip()
    if line == "":
        continue
    split_line = line.split(" ")
    
    move = split_line[0]
    if len(split_line) == 1:
        graph[move] = {}
    elif len(split_line) == 2:
        graph[move][split_line[1]] = None
    elif len(split_line) == 3:
        graph[move][split_line[1]] = split_line[2]
    else:
        print("Huh:", split_line)

def find_combos(option, seen):
    combo_tree = {}
    for next_option in graph[option]:
        if next_option not in seen:
            seen.add(next_option)
            combo_tree[next_option] = find_combos(next_option, seen.copy())
       
    
    return combo_tree

main_combo_tree = {}

for option in """U-Air
D-Air
B-Air
F-Air
N-Air
U-Tilt
D-Tilt
F-Tilt
Jab
Up-B
Side-B
Down-B
Neutral-B
F-Smash
D-Smash
U-Smash
Grab""".split("\n"):
    combos = find_combos(option, set())
    if combos:
        main_combo_tree[option] = combos

def print_tree(tree, indent=0):
    for item in tree:
        print(" "*indent, item, sep="")
        print_tree(tree[item], indent+1)
print_tree(main_combo_tree)


base_options="""
U-Air
Falling-U-Air
D-Air
Falling-D-Air
B-Air
F-Air
Tipper-F-Air
N-Air

U-Tilt
D-Tilt
F-Tilt
Jab

Up-B
Side-B
Down-B
Neutral-B

F-Smash
D-Smash
U-Smash

Grab
F-Throw
U-Throw
B-Throw
D-Throw

Grab F-Throw
Grab U-Throw
Grab B-Throw
Grab D-Throw



U-Air U-Air
U-Air D-Air
U-Air F-Air
U-Air N-Air
U-Air F-Smash

Falling-U-Air U-Air
Falling-U-Air F-Smash
Falling-U-Air D-Air

D-Air D-Air
D-Air Grab
D-Air F-Smash
D-Air Up-B

B-Air D-Air
B-Air F-Air

F-Air F-Air
F-Air N-Air
F-Air D-Air
F-Air U-Tilt
F-Air Up-B
F-Air F-Smash
F-Air D-Smash
F-Air Grab
F-Air Neutral-B

N-Air F-Air
N-Air D-Air
N-Air F-Smash
N-Air Up-B

U-Tilt D-Air
U-Tilt N-Air
U-Tilt B-Air
U-Tilt F-Air
U-Tilt U-Air
U-Tilt U-Air
U-Tilt F-Smash

D-Tilt Grab _

Side-B F-Air
Side-B U-Air
Side-B Up-B
Side-B U-Tilt
Side-B Side-B

U-Smash Grab
U-Smash F-Air
U-Smash F-Smash

F-Throw Grab _
F-Throw F-Smash _
F-Throw F-Air
F-Throw N-Air
F-Throw F-Tilt
F-Throw D-Air _
F-Throw D-Smash *

U-Throw Grab
U-Throw F-Air
U-Throw N-Air
U-Throw D-Air
U-Throw B-Air
U-Throw U-Air
U-Throw F-Smash

D-Throw Grab
D-Throw D-Air
D-Throw F-Air
D-Throw N-Air"""