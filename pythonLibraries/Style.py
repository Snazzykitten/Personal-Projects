""" Library to simply output pre-defined print functions to
    follow a organised color scheme. You may also use this
    library as an ASCI color chart. """

# =========================================================
# Style functions to rizz up the tty
# =========================================================

# A list containing ASCI escape sequences
ansi_colors = [
    '\033[0m',  # 0 - reset
    '\033[01m', # 1 - bold
    '\033[02m', # 2 - disable
    '\033[04m', # 3 - underline
    '\033[07m', # 4 - reverse
    '\033[08m', # 5 - invisible
    '\033[09m', # 6 - strikethrough

    '\033[30m', # 07 - fg black
    '\033[31m', # 08 - fg red
    '\033[32m', # 09 - fg green
    '\033[33m', # 10 - fg orange
    '\033[34m', # 11 - fg blue
    '\033[35m', # 12 - fg purple
    '\033[36m', # 13 - fg cyan
    '\033[37m', # 14 - fg lightgrey
    '\033[90m', # 15 - fg darkgrey
    '\033[91m', # 16 - fg lightred
    '\033[92m', # 17 - fg lightgreen
    '\033[93m', # 18 - fg yellow
    '\033[94m', # 19 - fg lightblue
    '\033[95m', # 20 - fg pink
    '\033[96m'  # 21 - fg lightcyan

    '\033[40m', # 22 - bg black
    '\033[41m', # 23 - bg red
    '\033[42m', # 24 - bg green
    '\033[43m', # 25 - bg orange
    '\033[44m', # 26 - bg blue
    '\033[45m', # 27 - bg purple
    '\033[46m', # 28 - bg cyan
    '\033[47m'  # 29 - bg lightgrey
]

# A list that converts the ASCI escape sequnces into a
# labled pairs, similar to a dictionary. It references the
# above list for the sake of simplicity to read.
colors_dict = [
    "reset", str(ansi_colors[0]),
    "bold", str(ansi_colors[1]),
    "disable", str(ansi_colors[2]),
    "underline", str(ansi_colors[3]),
    "reverse", str(ansi_colors[4]),
    "invisible", str(ansi_colors[5]),
    "strikethrough", str(ansi_colors[6]),

    "fg.black", str(ansi_colors[7]),
    "fg.red", str(ansi_colors[8]),
    "fg.green", str(ansi_colors[9]),
    "fg.orange", str(ansi_colors[10]),
    "fg.blue", str(ansi_colors[11]),
    "fg.purple", str(ansi_colors[11]),
    "fg.cyan", str(ansi_colors[12]),
    "fg.lightgrey", str(ansi_colors[13]),
    "fg.darkgrey", str(ansi_colors[14]),
    "fg.lightred", str(ansi_colors[15]),
    "fg.lightgreen", str(ansi_colors[16]),
    "fg.yellow", str(ansi_colors[17]),
    "fg.yellow", str(ansi_colors[18])
]

# =========================================================
# Defining functions
# =========================================================
def pprint(color, txt, style = "reset", query = False):
    """ Formatted as:
    pprint("<*1>", "MyText", style = "<*2>", query = Bool) 
    """
    # Each for loop iterates a value through the colors
    # colors list, until a matched pair is found with the
    # value, and the user's parameter. It is incremented by
    # one, as the above list is formatted ABABAB.
    for i in range(0, len(colors_dict), 2):
        if style == colors_dict[i]:
            style = colors_dict[i + 1]

    for i in range(0, len(colors_dict), 2):
        if color == colors_dict[i]:
            color = colors_dict[i + 1]
    
    # Checking if the output should include a input field
    if query == True:
        print(style, color, txt, ansi_colors[0], end="")
        temp = input()
        return temp
    else:
        print(style, color, txt)
    
# =========================================================
# Testing
# =========================================================

pprint("fg.blue", "What is yo name?", "bold", query=True)

#var = pprint("fg.red", "Hello World",style="reset",query=True)
#print(var, "HHC")