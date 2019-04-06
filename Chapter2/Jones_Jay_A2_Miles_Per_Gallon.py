# ============================================================
# PROGRAMMER:       Jay Jones
# PROGRAM NAME:     Assignment #02 - Variables & Calculations
# DATE WRITTEN:     March 30, 2019
# ============================================================
# INITIALIZE / DECLARE VARIABLES
milesPerGallon = 0.00

# ============================================================
# INPUT STATEMENTS
milesDriven = float(input("How many miles were driven? "))
gallonsUsed = float(input("How many gallons of gas were used? "))

# ============================================================
# PROCESSING / CALCULATIONS
milesPerGallon = milesDriven / gallonsUsed

# ============================================================
# OUTPUT STATEMENTS
print("Your Miles Per Gallon is: " + format(milesPerGallon, "9,.2f"))
