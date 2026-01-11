import sys

"""
Sources: 
https://stackoverflow.com/questions/57150426/what-is-printf
https://docs.python.org/3/library/sys.html#sys.argv
https://docs.python.org/3.4/library/stdtypes.html#str.strip

README in github
"""

def parse_file(filename):
    print(f"Reading {filename}")
    lines = []
    #opens file, strips out leading whitespace, and ignores comments; puts each line in a list
    for line in open(filename):
        li = line.strip()
        if li != "" and not li.startswith("#"):
            lines.append(li)
    # Uses first line in list to get number of choices
    num_choices = int(lines[0])
    print(f"Building {num_choices} x {num_choices} payoff...")
    # Uses second line in list to get game title
    game_title = lines[1]
    # labels and payoffs are made into a list so it can be printed easily
    labels = [game_title]
    payoff_matrix = []
    # for loop to parse 3rd and 4th lines
    for i in range(2, 2 + num_choices):
        parts = lines[i].split()
        # Strategy name is added to list
        labels.append(parts[0])
        # numbers are extracted to make tuples
        vals = [int(x) for x in parts[1:]]
        tuples = []
        for j in range(0, len(vals), 2):
            tuples.append((vals[j], vals[j + 1]))
        payoff_matrix.append(tuples)
    # prints third and fourth lines and formats as text
    print(f"Labels: {labels}")
    print(f"Payoffs: {payoff_matrix}")
    # returns values to be used later
    return num_choices, labels, payoff_matrix


# checks if file name contains three parts: python, nashEq.py, and -.txt
if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_file(sys.argv[1])
    else:
        print("Please provide a filename.")