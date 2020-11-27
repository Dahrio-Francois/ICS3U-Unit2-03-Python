#!/usr/bin/env python 3

# Created by: Dahrio Francois
# Created on: November 2020
# this program calculates the circumference of a circle using tau
#     with user input


import constants


def main():
    # this program calculates circumference

    # input
    radius = int(input("Enter radius of circle (mm): "))

    # process
    circumference = constants.TAU*radius

    # output
    print("")
    print("Circumference is {}mm^2".format(circumference))


if __name__ == "__main__":
    main()
