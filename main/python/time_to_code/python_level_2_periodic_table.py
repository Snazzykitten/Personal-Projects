# --------------------
""" Periodic Table """
#---------------------


# --------------------
# Subprograms
# --------------------
def periodic_table(symbol_of_element):
    """ Indexes and identifies data within the periodic table """

    class Element:
        """ Contains data for periodic elements  """

        Li = ["Li", "Lithium", 6.94, "Alkali metals"]
        Na = ["Na", "Sodium", 22.99, "Alkali metals"]
        K = ["K", "Potassium", 39.098, "Alkali metals"]
        F = ["F", "FLuorine", 18.998, "Halogens"]
        Cl = ["Cl", "Chlorine", 35.45, "Halogens"]
        Br = ["Br", "Bromine", 79.904, "Halogens"]

    if symbol_of_element == str.lower("li"):
        symbol = Element.Li[0]
        element = Element.Li[1]
        atomic_weight = Element.Li[2]
        group = Element.Li[3] 
       
    return(str(symbol) + " " + str(element) + " " + str(atomic_weight) + " " + str(group))


# --------------------
# Main Program
# --------------------
user_choice = input("Enter a elements symbol: ")
print(periodic_table(user_choice))
