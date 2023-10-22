# ---------------------------
""" Energy bill calulator """
# ---------------------------


# ---------------------------
# Subprograms
# ---------------------------
def energy_cost(previous_meter_reading, current_meter_reading, calorific_value):
    """ Calculates energy bill, returns the cost """
    units_used = current_meter_reading - previous_meter_reading
    kilowatt_hours = units_used * 1.022 * (calorific_value / 3.6)
    cost = 0.0284 * kilowatt_hours
    return cost


# ---------------------------
# Main program
# ---------------------------

# Constants
CALORIFIC_VALUE = 39.3

# Assigning variables
previous_meter_reading = int(input("Enter the previous meter reading as a four digit integer: "))
current_meter_reading = int(input("Enter the current meter reading as a four digit integer: "))

# Calculating the energy bill
print("Cost is £", int(energy_cost(previous_meter_reading, current_meter_reading, CALORIFIC_VALUE)))


