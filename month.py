#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: March 30th, 2025
# This program asks the user to enter a integer
# for a month but it should be between 1 and 12.


def main():

    month_as_integer = input("Enter a number for a month: ")

    match month_as_integer:

        case "1":
            print(month_as_integer + " is January")

        case "2":
            print(month_as_integer + " is February")

        case "3":
            print(month_as_integer + " is March")

        case "4":
            print(month_as_integer + " is April")

        case "5":
            print(month_as_integer + " is May")

        case "6":
            print(month_as_integer + " is June")

        case "7":
            print(month_as_integer + " is July")

        case "8":
            print(month_as_integer + " is August.")

        case "9":
            print(month_as_integer + " is September.")

        case "10":
            print(month_as_integer + " is October.")

        case "11":
            print(month_as_integer + " is November.")

        case "12":
            print(month_as_integer + " is December.")

        case _:
            print("Your input is an invalid month.")


if __name__ == "__main__":
    main()
