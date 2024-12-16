class PrettyLogger:
    i = 0
    reset = "\033[0m"

    def colors():
        numbers = [
            1,
            2,
            3,
            4,
            5,
            6,
            196,
            154,
            228,
            27,
        ]
        return [f"{number}" for number in numbers]

    def pretty(text, color, end=None):
        prefix = "\033[38;5;"
        print(f"{prefix}{color}m{text}{PrettyLogger.reset}", end="", flush=True)

    def logId(text, id):
        colors = PrettyLogger.colors()
        PrettyLogger.pretty(text, colors[id % len(colors)])

    def log(text):
        PrettyLogger.logId(text, PrettyLogger.i)
        PrettyLogger.i = PrettyLogger.i + 1


log = PrettyLogger.log
logId = PrettyLogger.logId


def across(startRow, startCol):
    return [[startRow, col] for col in range(startCol, startCol + 4)]


def down(startRow, startCol):
    return [[row, startCol] for row in range(startRow, startRow + 4)]


def downAcrossDiagonally(startRow, startCol):
    return [[startRow + i, startCol + i] for i in range(0, 4)]


def downLeftDiagonally(startRow, startCol):
    return [[startRow + i, startCol - i] for i in range(0, 4)]


sampleMatches = [
    downAcrossDiagonally(0, 4),
    across(0, 5),
    across(1, 1),
    down(1, 6),
    downAcrossDiagonally(2, 3),  # same starting point with below - interesting!
    downLeftDiagonally(2, 3),
    down(3, 9),
    downLeftDiagonally(3, 9),
    across(4, 0),
    across(4, 3),
    downAcrossDiagonally(6, 0),
    downAcrossDiagonally(6, 2),
    downLeftDiagonally(6, 4),
    downLeftDiagonally(6, 6),  # same starting point with below - interesting!
    downAcrossDiagonally(6, 6),
    downLeftDiagonally(6, 8),
    down(6, 9),
    across(9, 6),
]
foundXmases = []

enabledFiles = ["day4-1-sample.txt", "day4.txt"]


# get the rows and columns which have xmas in them
def findXmas(block: list[str]):
    xmases = []
    # possible paths:
    # across
    # across reverse
    # down
    # down reverse (same as up)
    # down across diagonally
    # down across diagonally reverse (same as up left)
    # down left diagonally
    # down left diagonally reverse (same as up across)
    rowEnum = enumerate(block)
    for row, text in rowEnum:
        colEnum = enumerate(text)
        # I probably don't need to iterate over literally every character as i don't even use the chars.
        # could rewrite this to ranges
        for col, char in colEnum:
            ranges = [
                across(row, col),
                down(row, col),
                downAcrossDiagonally(row, col),
                downLeftDiagonally(row, col),
            ]
            for range in ranges:
                word = ""
                for testRow, testCol in range:
                    if testRow < 0 or testCol < 0 or testCol > len(text) - 1:
                        continue
                    try:
                        word += block[testRow][testCol]
                    except:
                        pass
                if word == "XMAS" or word == "SAMX":
                    xmases += [range]

    return xmases


for file in enabledFiles:
    with open(file) as f:
        PrettyLogger.pretty(f"Ho ho ho! Reading file  {file} for XMASes!\n", "28")

        # for line in f:
        lines = [line for line in f]
        # for i in range(0, len(lines) - 4):
        # foundXmases += findXmas(lines[i : i + 4 :])
        # blockwise optimization is possible
        foundXmases = findXmas(lines)
        for idLine, line in enumerate(lines):
            PrettyLogger.pretty(f"L {idLine}".ljust(6), "255")
            for idChar, char in enumerate(line):
                try:
                    m = [x for x in foundXmases if [idLine, idChar] in x][0]
                    color = foundXmases.index(m)
                    logId(char, color)
                except:
                    print(".", end="", flush=True) if char != "\n" else print()
                    continue
        PrettyLogger.pretty(f"\n\nFound {len(foundXmases)} XMASes!\n\n", "42")
