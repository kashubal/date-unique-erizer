#!/usr/bin/env python3

"""DATE UNIQUE-ERIZER will read a list of input dates and output a list of unique dates.

This application will read a specified input file, expecting a list of date 
values.  The data values will then be normalized, sorted, and assessed for 
uniqueness.  The unique list of dates will then be written to the specified
output file. 

Usage example:

  python dateunique.py

The application will prompt the user for necessary inputs:
  complete or relative path to input file containing date values
  complete or relative path to output file to which results will be written
"""

import numpy as np
import sys
import os
from datetime import datetime
from dateutil import parser


print("********************")
print("********************")
print("DATE UNIQUE-ERIZER")
print("********************")
print("********************")
print()
print("This application will read a specified input file, expecting a "
    "list of date values.  The data values will then be normalized, "
    "sorted, and assessed for uniqueness.  The unique list of dates "
    "will then be written to the specified output file.")

# prompt user for input file
print()
input_file_location = str(input("Please enter the full path to your input "
    "file or, if in the current directory, the file name: ")) or "dates.txt"
print("Input file name/location you provided:" + input_file_location)

# prompt user for output file
print()
output_file_location = str(input("Please enter the full path to your "
    "output file or, if in the current directory, the file name: ")
    ) or "datesout.txt"
print("Output file name/location you provided:" + output_file_location)

# read in data inputs from user-provided input file and store in list
input_dates = []
with open(input_file_location) as input_file:
    input_dates = [line.strip() for line in input_file]
input_file.close()

# normalize date values, convert to iso format, and store in list
normalized_dates = []
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
for date in input_dates:
    try:
        # use dateutil parser to normalize different date formats
        # then add to list of strings using the format defined
        normalized_dates.append(parser.parse(date).strftime(DATE_FORMAT))
    except:
        # dateutil.parser is pretty good at figuring out what
        # date values are intended, but the user could still 
        # supply a value is completely irrelevant;  catch that
        # and just toss out those values, but let the user know!
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("WARNING:  Non-date values found in input file!  These "
            "values will be discarded.  The final list will only include "
            "valid date values.")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# determine unique dates and sort
normalized_dates = np.unique(normalized_dates)

# print list of dates to the console if size of list is less than 100,
# otherwise just print to output file to avoid the noise
if len(normalized_dates)<=100:
    print("\n\nHere's your list of unique, sorted dates:")
    print(normalized_dates)
else:
    print("There are more than 100 unique dates in the final list.  DATA "
        "UNIQUE-ERIZER will not print the list to the console so it can "
        "avoid filling up your screen.  Please refer to output file for "
        "list of dates.")

# open output file and write out date values
with open(output_file_location,"w") as output_file:
    print("********************", file=output_file)
    print("********************", file=output_file)
    print("DATE UNIQUE-ERIZER", file=output_file)
    print("********************", file=output_file)
    print("********************", file=output_file)
    print()
    print("This is the output file generated from the DATE UNIQUE-ERIZER "
        "utility.  The contents of this file represent the unique date "
        "values read in from the input file " + input_file_location + 
        " as of " + datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z'),
        file=output_file)
    print("\n\nInput values:", file=output_file)
    print(input_dates, file=output_file)
    print("\n\nUnique Date Values:", file=output_file)
    # print date values
    for date in normalized_dates:
         print(date, file=output_file)
    print("\n\nThat's all of the unique date values found!", file=output_file)
output_file.close()

# let user know we're done
print("\nThe output file " + output_file_location + " has been generated.")
print("\nThanks for using DATE UNIQUE-ERIZER!")

sys.exit()