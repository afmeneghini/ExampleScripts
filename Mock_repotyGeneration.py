"""
Chapter 11 Assignment
Author: Aaron Meneghini
Course: Python Programming
Date: 20171002

Description:
    A school committee is preparing a propsal for a request to
    increase the eduction budget for a town meeting. Your are
    contracted to prepare the report and getting the statistics
    of students' growth frim 2008 to 2009 is one of the tasks.
    You have two text files to get student data. Each file contains
    registered student numbers for each school of the town, and
    there are ten schools in this town.

    The text files contain comma-seperated values, listed in the
    following order: school-id1, students_number1, school_id2,
    students_number2....

    Deliverables:
        A python program that can read the two text files and
    generates a report saved in a formatted text file,
    containing the following information:
    School ID   # of Student(09)    # of student(08)    growth
    1               xxxxx             xxxxxx              xx
    2               xxxxx             xxxxxx              xx
    ...             xxxxx             xxxxxx              xx
    10              xxxxx             xxxxxx              xx
    --------------------------------------------------------------
    Total:
    Growth Rate: xx.xx%

    The following formula is used for evaluating growth rate (in %):

    total of 09 - total of 08 / total of 08 *100

    """
import csv #importing the tools of csv management 
import string #importing the string module
import itertools #importing the itertools module
import collections # don't know that I need this
import copy

Path = r'c:\Users\Aaron\Desktop\Python Programming\\' # Path to the first csv file
strName_one = "ch11_assignment_prob2_2008.csv" # Name of the first csv file
stripathname_one = Path+strName_one #combination of path and name of 2008 csv
   
Path_two = r'c:\Users\Aaron\Desktop\Python Programming\\' # Path to the second csv file
strName_two = "ch11_assignment_prob2_2009.csv" # Name of the second csv file
stripathname_two = Path_two+strName_two # combination of path and name of 2009 csv

f = open(stripathname_one, "r") # open the 2008 data
x = f.read() # assigning the read values of 2008 data to variable x
f.close() #closing that file

f = open (stripathname_two, "r") #open 2009 data
y = f.read() #assigning the read values of the 2009 data to variable y
f.close() #close 2009 data

x_split = string.split(x, ",") # conversion of string to list
y_split = string.split(y, ",") # conversion of string to list

school_ID = x_split[::2] # list of school ID values
school_ID_int = map(int, school_ID)

d_x = dict(itertools.izip_longest(*[iter(x_split)]*2, fillvalue="")) #conversion of list to dictionary 2008
d_y = dict(itertools.izip_longest(*[iter(y_split)]*2, fillvalue="")) #conversion of list to dictionary 2009

def Sortedvalues2008(x):
    for k in sorted(d_x): # attempts at sorting the dictionaries TT_TT
        print d_x[k]
    
def Sortedvalues2009 (x):
    for k in sorted(d_y): # attempts at sorting the dictionaries TT_TT
        print d_y[k]

d_x_int = dict((int(k), int(v)) for k, v in d_x.iteritems()) # turning the strings into integers in the x dictionary
d_y_int = dict((int(k), int(v)) for k, v in d_y.iteritems()) # turning the strings into integers in the x dictionary

heading = "School ID\tNumber of Students (09)\tNumber of Students (08)\tGrowth"
One_values = []
two_values = []
def dx_values_matched_to_ID(x):
    one = []
    for k in school_ID_int:
        if k in d_x:
            one = [k]
        print one
            
                     

def dy_values_matched_to_ID(x):
    for k in school_ID:
        if k in d_y:
            print d_y[k]
print dx_values_matched_to_ID(school_ID_int)


j= list(d_x_int.keys()) # list of keys (should only need this once)
h = list(d_x_int.values()) # list of values for 08
g = list(d_y_int.values()) # list of values for 09

G = list(d_x.keys())  #string list of keys
H = list(d_x.values()) # string list of 2008 values
A = heading

def row_one (x): # definition of the header for the table
    print x
row_one(heading) # callback

print 
for row in map(): # joining string lists into a table!
    print '\t'.join(row)

dx_values_matched_to_ID(school_ID),"\t",dy_values_matched_to_ID(school_ID)

