import sys
from Player import *
from rpsPlayer import *
import ternary
import matplotlib.pyplot as plt


"""
Sources: 
https://stackoverflow.com/questions/57150426/what-is-printf
https://docs.python.org/3/library/sys.html#sys.argv
https://docs.python.org/3.4/library/stdtypes.html#str.strip
https://www.geeksforgeeks.org/python/python-list-slicing/
https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
README in github
"""

def parse_file(filename):
    """
    Parses file from given filename; opens file and parses line by line
    Args: filename: name of file to parse
    Returns: title of name of game and a matrix comprising possible values of game
    Logs information and prints out exactly the same as in instructions:
    Reading file.txt
    Building n x n payoff...
    Labels: ['game', 'strategy1', 'strategy-n-1', 'strategy-n']
    Payoffs: [insert number tuples here]
    """
    print("Reading " + filename)
    lines = []
    #opens file, strips out leading whitespace, and ignores comments; puts each line in a list
    for line in open(filename):
        li = line.strip()
        if li != "" and not li.startswith("#"):
            lines.append(li)
    # Uses first line in list to get number of choices
    num = int(lines[0])
    game_title = lines[1]
    print(f"Building {num} x {num} payoff...")
    # Uses second line in list to get game title
    # labels and payoffs are made into a list so it can be printed easily
    labels = [game_title]
    payoff_matrix = []
    # for loop to parse 3rd and 4th lines
    for i in range(2, 2 + num):
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
    return game_title, payoff_matrix


def run_2x2(matrix):
    """
    Runs 2x2 matrix (pd, bos, stag)
    Args: matrix: 2x2 matrix
    Returns: players: created list of players with logged history of preferences
    Runs game on each player for 2250 rounds using round-robin logic
    In every game a strategy is picked, outcome is decided, preferences are changed
    history is then updated to be plotted later
    """
    players = []
    for i in range(10):
        # Creates and adds player
        player_name = "P" + str(i + 1)
        p = Player(player_name)
        players.append(p)
    # 50 sessions fo 2250 total rounds
    for session in range(50):
        # everyone plays each other
        for i in range(10):
            for j in range(i + 1, 10):
                p1 = players[i]
                p2 = players[j]
                # Gets strategy
                s1 = p1.getStrategy()
                s2 = p2.getStrategy()
                # Gets payoffs
                payoff1, payoff2 = matrix[s1][s2]
                # Updates score and preferences
                p1.updateScore(payoff1)
                p1.updatePrefs(s1, payoff1)
                p2.updateScore(payoff2)
                p2.updatePrefs(s2, payoff2)
    return players


def plot_pd(playerA, playerB):
    """
    scatter plots preference histories of two players in prisoners dilemma
    Args: playerA: first player; playerB: second player
    Creates matplotlib plot with preference histories of both players plotted to convergence
    """
    # gets player history and plots to get preference
    x = playerA.history[::10]
    x1 = playerA.history2[::10]
    y = playerB.history[::10]
    y1 = playerB.history2[::10]
    # make sizes increase
    sizes = []
    for i in range(len(x)):
        sizes.append(20 * i)
    plt.figure(figsize = (8, 8))
    plt.scatter(x, x1, s = sizes, alpha = 0.5, c = 'blue', label = f'{playerA.id}')
    plt.scatter(y, y1, s = sizes, alpha = 0.5, c = 'yellow', label = f'{playerB.id}')
    plt.title(f"Prisoners Dilemma")
    plt.xlabel("quiet")
    plt.ylabel("confess")
    plt.xlim(-0.05, 0.55)
    plt.ylim(0.45, 1.05)
    # adds gridlines
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_bos(playerA, playerB):
    """
    scatter plots preference histories of two players in battle of the sexes
    Args: playerA: first player; playerB: second player
    Creates matplotlib plot with preference histories of both players plotted to convergence
    """
    # gets player history and plots to get preference
    x = playerA.history[::10]
    x1 = playerA.history2[::10]
    y = playerB.history[::10]
    y1 = playerB.history2[::10]
    # make sizes increase
    sizes = []
    for i in range(len(x)):
        sizes.append(20 * i)
    plt.figure(figsize=(8, 8))
    plt.scatter(x, x1, s = sizes, alpha = 0.5, c = 'purple', label = f'{playerA.id}')
    plt.scatter(y, y1, s = sizes, alpha = 0.3, c = 'blue', label = f'{playerB.id}')
    plt.title(f"Battle of Sexes")
    plt.xlabel("opera")
    plt.ylabel("football")
    plt.xlim(-0.05, 1.05)
    plt.ylim(-0.05, 1.05)
    # adds gridlines
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_stag(playerA, playerB):
    """
    scatter plots preference histories of two players in stag and hunt game
    Args: playerA: first player; playerB: second player
    Creates matplotlib plot with preference histories of both players plotted to convergence
    """
    # gets player history and plots to get preference
    x = playerA.history[::10]
    x1 = playerA.history2[::10]
    y = playerB.history[::10]
    y1 = playerB.history2[::10]
    # make sizes increase
    sizes = []
    for i in range(len(x)):
        sizes.append(20 * i)
    plt.figure(figsize = (8, 8))
    plt.scatter(x, x1, s = sizes, alpha = 0.5, c = 'pink', label = f'{playerA.id}')
    plt.scatter(y, y1, s = sizes, alpha = 0.3, c = 'green', label = f'{playerB.id}')
    plt.title(f"Stag and Hunt Game")
    plt.xlabel("stag")
    plt.ylabel("hunt")
    plt.xlim(-0.05, 1.05)
    plt.ylim(-0.05, 1.05)
    # adds gridlines
    plt.grid(True)
    plt.legend()
    plt.show()

#---------------------------------------------------
def run_rps(matrix):
    """
    Runs 3x3 rps matrix
    Args: matrix: rps matrix
    Returns: players: created list of players with logged history of preferences
    Similar logic to run2x2 but applies to rps now
    Does not do round-robin but can be modified to do so by changing the 2s to n-s
    """
    players = []
    for i in range(2):
        # Creates and adds player
        player_name = "P" + str(i + 1)
        p = rpsPlayer(player_name)
        players.append(p)
    # Same logic but runs for two people playing and 10k times
    for session in range(10000):
        for i in range(2):
            for j in range(i + 1, 2):
                p1, p2 = players[i], players[j]
                s1, s2 = p1.getStrategy(), p2.getStrategy()
                payoff1, payoff2 = matrix[s1][s2]
                p1.updateScore(payoff1)
                p1.updatePrefs(s1, payoff1)
                p2.updateScore(payoff2)
                p2.updatePrefs(s2, payoff2)
    return players


def plot_rps(playerA, playerB):
    """
    scatter plots preference histories of two players in rock paper scissors
    Args: playerA: first player; playerB: second player
    Creates triangle matplotlib plot using ternary with preference histories of both players plotted to show patterns
    """
    ##Boundary and Gridlines
    scale = 1.0
    figure, tax = (ternary.figure (scale = scale))
    # Draw Boundary and Gridlines
    tax.boundary(linewidth = 1)
    tax.gridlines(color = "black", multiple = 0.1, alpha = 1)
    tax.scatter(playerA.history, color = "orange", label = f"{playerA.id}", alpha = 0.04)
    tax.scatter(playerB.history, color = "green", label = f"{playerB.id}", alpha = 0.03)
    tax.set_title("RPS")
    tax.bottom_axis_label("Rock")
    tax.right_axis_label("Paper", offset = 0.1)
    tax.left_axis_label("Scissors", offset = 0.1)
    tax.ticks(axis = "lbr", multiple = 0.2, linewidth = 1, tick_formats = "%.1f")
    # erases matplotlib square
    tax.get_axes().axis("off")
    tax.legend()
    ternary.plt.show()


def main():
    """
    Runs the code, allows it to be run from local terminal
    calls other methods to plot
    """
    if len(sys.argv) < 2:
        print("Works; use command line and run: python nashEq.py + filename.txt")
        return
    filename = sys.argv[1]
    game_name, matrix = parse_file(filename)
    if game_name == "Prisoner's Dilemma":
        # Run simulation
        pd_players = run_2x2(matrix)
        print("\nFinal Preferences:")
        for p in pd_players:
            print(p)
        # Generates 5 plots
        matchups = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
        for m in matchups:
            plot_pd(pd_players[m[0]], pd_players[m[1]])
    elif game_name == "Battle of the Sexes":
        # Run simulation
        bos_players = run_2x2(matrix)
        print("\nFinal Preferences:")
        for p in bos_players:
            print(p)
        # Generates 5 plots
        matchups = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
        for m in matchups:
            plot_bos(bos_players[m[0]], bos_players[m[1]])
    elif game_name == "Stag Hunt":
        # Run simulation
        stag_players = run_2x2(matrix)
        print("\nFinal Preferences:")
        for p in stag_players:
            print(p)
        # Generates 5 plots
        matchups = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
        for m in matchups:
            plot_stag(stag_players[m[0]], stag_players[m[1]])
#---------------------------------------------------
    elif game_name == "Rock Paper Scissors":
        # Run simulation
        rps_players = run_rps(matrix)
        print("\nFinal Preferences:")
        for p in rps_players:
            print(p)
        plot_rps(rps_players[0], rps_players[1])


"""
python nashEq.py pd.txt
python nashEq.py bos.txt
python nashEq.py stag.txt
python nashEq.py rps.txt
"""


if __name__ == "__main__":
    main()