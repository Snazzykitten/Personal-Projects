""" Traffic light responder """

# Defining function classes
class Colors:
    """ Prints color response """
    def red(self):
        """ Wait! """
        print("Wait!")

    def orange(self):
        """ Get Ready... """
        print("Get Ready...")

    def green(self):
        """ Go! """
        print("Go!")

# Asking for input
var1 = str.lower(input("Choose a traffic light color: "))

# Printing color response
if var1 == "red":
    Colors.red(1)
elif var1 == "orange":
    Colors.orange(2)
else:
    Colors.green(3)
