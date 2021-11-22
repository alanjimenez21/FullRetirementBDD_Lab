"""
*Name: Alan Ivan Jimenez Gallardo
*Instructor: Phillip Enkema
*Assignment: Lab01
*Due: 08/22/2021

*Write and debug a Python program
Decompose a problem into modules that isolate the user interface from the retirement age calculation
Analyze user input to select the correct calculation for Full Retirement Age
"""
import datetime
import sys

#Program correctly calculates the age and additional months for Full Retirement Age
def retirement_calculation():
    while (True):
        birth_year = input("\nEnter the year of birth or Enter to exit: ")
        # Using sys.exit to terminte the prorgam
        if birth_year == "":
            sys.exit("Process finished with exit code 0")

        #Program correctly calculates the year and month for Full Retirement Age
        else:
            # Variables
            birth_year = int(birth_year)
            birth_month = int(input("Enter the month of birth: "))
            current_year = datetime.datetime.now().strftime("%Y")

            # Process to get people from 1900 to 1942
            if (birth_year <= 1937 and birth_year > 1899):
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 65 and 0 months.")
                print("This will be in {} of".format(month) + " {}".format(birth_year + 65))
            elif (birth_year == 1938):
                birth_month = 2 + birth_month
                # Code for months that are greater than 12 - Example 13 = January
                # Explanation - If the moenth happens to be January we have to increse the year
                # Continue - substract the 12 and just leave the number.
                if (birth_month > 12):
                    birth_month = birth_month - 12
                    birth_year = birth_year + 1
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 65 and 2 months.")
                print("This will be in {} of".format(month) + " {}".format((birth_year + 65)))
            elif (birth_year == 1939):
                birth_month = 4 + birth_month
                # Code
                if (birth_month > 12):
                    birth_month = birth_month - 12
                    birth_year = birth_year + 1
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 65 and 4 months.")
                print("This will be in {} of".format(month) + " {}".format((birth_year + 65)))
            elif (birth_year == 1940):
                birth_month = 6 + birth_month
                # Code
                if (birth_month > 12):
                    birth_month = birth_month - 12
                    birth_year = birth_year + 1
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 65 and 6 months.")
                print("This will be in {} of".format(month) + " {}".format((birth_year + 65)))
            elif (birth_year == 1941):
                birth_month = 8 + birth_month
                if (birth_month > 12):
                    birth_month = birth_month - 12
                    birth_year = birth_year + 1
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 65 and 8 months.")
                print("This will be in {} of".format(month) + " {}".format((birth_year + 65)))
            elif (birth_year == 1942):
                birth_month = 10 + birth_month
                # Code
                if (birth_month > 12):
                    birth_month = birth_month - 12
                    birth_year = birth_year + 1
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 65 and 10 months.")
                print("This will be in {} of".format(month) + " {}".format((birth_year + 65)))
            # Process for 1943 - 1954
            elif (birth_year >= 1943 and birth_year <= 1954):
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 66 and 0 months.")
                print("This will be in {} of".format(month) + " {}".format((birth_year + 65)))
            # Process for 1955 - 1959
            elif (birth_year == 1955):
                birth_month = 2 + birth_month
                # Code
                if (birth_month > 12):
                    birth_month = birth_month - 12
                    birth_year = birth_year + 1
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 66 and 2 months.")
                print("This will be in {} of".format(month) + " {}".format((birth_year + 65)))
            elif (birth_year == 1956):
                birth_month = 4 + birth_month
                # Code
                if (birth_month > 12):
                    birth_month = birth_month - 12
                    birth_year = birth_year + 1
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 66 and 4 months.")
                print("This will be in {} of".format(month) + " {}".format((birth_year + 65)))
            elif (birth_year == 1957):
                birth_month = 6 + birth_month
                # Code
                if (birth_month > 12):
                    birth_month = birth_month - 12
                    birth_year = birth_year + 1
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 66 and 6 months.")
                print("This will be in {} of".format(month) + " {}".format((birth_year + 65)))
            elif (birth_year == 1958):
                birth_month = 8 + birth_month
                # Code
                if (birth_month > 12):
                    birth_month = birth_month - 12
                    birth_year = birth_year + 1
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 66 and 8 months.")
                print("This will be in {} of".format(month) + " {}".format((birth_year + 65)))
            elif (birth_year == 1959):
                birth_month = 10 + birth_month
                # Code
                if (birth_month > 12):
                    birth_month = birth_month - 12
                    birth_year = birth_year + 1
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                print("Your full retirement is age 66 and 10 months.")
                print("This will be in {} of".format(month) + " {}".format((birth_year + 65)))
            elif (birth_year >= 1960):
                month = datetime.date(1900, birth_month, 1).strftime('%B')
                # Code
                print("Your full retirement is age 67 and 0 months.")
                print("This will be in {} of".format(month) + " {}".format(birth_year + 67))

#Program structure separates the code interacting with the user from the Full Retirement Age calculations
print("Social Security Full Retirement Age Calculator:")
calculation = retirement_calculation()
