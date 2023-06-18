###############################################################################
# CMPT 145 Course material
# Original Author: Lauresa Stilling
# Date Created:   31 May 2023
# Last Edited:    31 May 2023
#
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Testing; relevant to Chapter 5, 6, 7
###############################################################################

# TODO: Fill in your information below
# Student Name: Hatem Alfarra
# NSID: Hma194
# Student Number: 11291988

################### DO NOT ALTER CODE BELOW ###################################
def gcd(val1: int, val2: int) -> int:
    """
    Purpose: Find the greatest common divisor (gcd) of the two values passed in.
    Pre-conditions:
        :param val1: int - integer value being compared to find gcd.
            Must be less than 1000, else returns -1
        :param val2: int - integer value being compared to find gcd
            Must be less than 1000, else returns -1
    Post Conditions:
        None
    Return:
        int - The greatest common positive divisor of the two numbers passed in.
            -1 returned on failure.
    """
    return -1


def replace(input_str: str, target: str, replacement: str) -> str:
    """
    Purpose: Replace all instances of target string with replacement string within input string.
        Starting at the first occurrence of target string.
    Pre-condition
        :param input_str:str - input string to change target strings to replacement strings
        :param target: str - string that one wishes to change, if empty will return original string uncahnged.
        :param replacement: str - string that will replace target strings in the input string
    Post Condition:
        None
    Return:
        str - new string where target strings have been changed to replacement string
    """
    new_str = ""
    inp_len = len(input_str)
    targ_len = len(target)
    if inp_len < targ_len or targ_len==0:
        new_str = input_str
    else:
        i = 0
        while i < inp_len:
            if input_str[i:i+targ_len] == target:
                new_str += replacement
                i += targ_len
            else:
                new_str += input_str[i]
                i += 1
    return new_str


def grade_letter(score:int) -> str:
    """
    Purpose: Get the grade letter related to the score passed in.

    Pre-condition
        :param score:int - the number being calculated to a letter grade.
            Should be within the range of 0-100
    Post Condition:
        None
    Return:
        str - string associated with the score passed in
            if score is outside valid range returns the string "Invalid"
    """
    letter = ""
    if score < 0 or score > 100:
        letter = "Invalid"
    elif score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"
    return letter

def sort_students_into_grades(student_list: list) -> dict:
    """
    Purpose: Goes through a list of dictionaries adding student names to the appropriate dictionary grade letter
        If the student's grade is not one of "A", "B", "C", "D", or "F", it is added to list "Invalid".
    Pre-condition:
        :param student_list: list of dictionaries,
            each dictionary represents a student and contains two keys: 'name' and 'grade'
    Post Condition:
        None
    Return:
        dict with lists as values; each key has a list value of names of students with that grade letter.
            Contains the keys "A","B","C","D","F","Invalid"
    """
    return {}
################### DO NOT ALTER CODE ABOVE ###################################


# TODO: Create tests for functions above

# Testing function gcd().

# Test 1: Correct/valid arguments into the function.
def gcd_test1():
    parameter_1 = 12
    parameter_2 = 8
    result = gcd(parameter_1, parameter_2)
    expected = 4
    if result != expected:
        print("Test case 1 failed. where the parameters", parameter_1, "and", parameter_2, "output:", result, "instead of the expected number:", expected)


# Test 2: first argument being smaller with valid parameters.
def gcd_test2():
    parameter_1 = 8
    parameter_2 = 12
    result = gcd(parameter_1, parameter_2)
    expected = 4
    if result != expected:
        print("Test case 2 failed. where the parameters", parameter_1, "and", parameter_2, "output:", result, "instead of the expected number:", expected)


# Test 3: First argument being above 1000.
def gcd_test3():
    parameter_1 = 1002
    parameter_2 = 8
    result = gcd(parameter_1, parameter_2)
    expected = -1
    if result != expected:
        print("Test case 3 failed. where the parameters", parameter_1, "and", parameter_2, "output:", result, "instead of the expected number:", expected)


# Test 4: Second argument being above 1000.
def gcd_test4():
    parameter_1 = 12
    parameter_2 = 1002
    result = gcd(parameter_1, parameter_2)
    expected = -1
    if result != expected:
        print("Test case 4 failed. where the parameters", parameter_1, "and", parameter_2, "output:", result, "instead of the expected number:", expected)


# Test 5: Arguments passed are negative
def gcd_test5():
    parameter_1 = -12
    parameter_2 = -24
    result = gcd(parameter_1, parameter_2)
    expected = 12
    if result != expected:
        print("Test case 5 failed. where the parameters", parameter_1, "and", parameter_2, "output:", result, "instead of the expected number:", expected)




# Testing the function replace():


# Test 1: Valid arguments for parameters.
def replace_test1():
    parameter_1 = "Test1"
    parameter_2 = "1"
    parameter_3 = "A"
    result = replace(parameter_1, parameter_2, parameter_3)
    expected = "TestA"
    if result != expected:
        print("Test case 4 failed. where the parameters", parameter_1 + ",", parameter_2, "and", parameter_3, "output:", result, "instead of the expected:", expected)

# Test 2: Empty strings tested.
def replace_test2():
    parameter_1 = ""
    parameter_2 = ""
    parameter_3 = ""
    result = replace(parameter_1, parameter_2, parameter_3)
    expected = ""
    if result != expected:
        print("Test case 4 failed. where the parameters", parameter_1 + ",", parameter_2, "and", parameter_3, "output:", result, "instead of the expected:", expected)

# Test 3: String to be replaced is not in the searched text.
def replace_test3():
    parameter_1 = "1234"
    parameter_2 = "5"
    parameter_3 = "not 5"
    result = replace(parameter_1, parameter_2, parameter_3)
    expected = "1234"
    if result != expected:
        print("Test case 4 failed. where the parameters", parameter_1 + ",", parameter_2, "and", parameter_3, "output:", result, "instead of the expected:", expected)


# Test 4: The string to be replaced is repeated more than once in the searched string.
def replace_test4():
    parameter_1 = "122"
    parameter_2 = "2"
    parameter_3 = "1"
    result = replace(parameter_1, parameter_2, parameter_3)
    expected = "111"
    if result != expected:
        print("Test case 4 failed. where the parameters", parameter_1 + ",", parameter_2, "and", parameter_3, "output:", result, "instead of the expected:", expected)


# Test 5: The text to be replaced is empty.
def replace_test5():
    parameter_1 = "123"
    parameter_2 = "2"
    parameter_3 = ""
    result = replace(parameter_1, parameter_2, parameter_3)
    expected = "13"
    if result != expected:
        print("Test case 5 failed. where the parameters", parameter_1 + ",", parameter_2, "and", parameter_3, "output:", result, "instead of the expected:", expected)





# Testing the function grade_letter():


# Test 1: Grade is 95. Testing a valid answer
def grade_letter_test1():
    parameter_1 = 95
    result = grade_letter(parameter_1)
    expected = "A"
    if result != expected:
        print("Test case 1 failed. where the parameter", parameter_1, "output:", result, "instead of the expected:", expected)


# Test 2: Grade is 0. Testing the boundaries (The lowest possible valid number).
def grade_letter_test2():
    parameter_1 = 0
    result = grade_letter(parameter_1)
    expected = "F"
    if result != expected:
        print("Test case 2 failed. where the parameter", parameter_1, "output:", result, "instead of the expected:", expected)


# Test 3: Grade is -1. Testing an invalid number (negative integer)
def grade_letter_test3():
    parameter_1 = -1
    result = grade_letter(parameter_1)
    expected = "Invalid"
    if result != expected:
        print("Test case 3 failed. where the parameter", parameter_1, "output:", result, "instead of the expected:", expected)


# Test 4: Grade is 80. Testing a multiple of 10 above 50. 80 should be a B rather than a C or an A.
def grade_letter_test4():
    parameter_1 = 90
    result = grade_letter(parameter_1)
    expected = "A"
    if result != expected:
        print("Test case 4 failed. where the parameter", parameter_1, "output:", result, "instead of the expected:", expected)


# Test 5: Grade is 90. Testing that the output of the function letter_grade() is a string
def grade_letter_test5():
    parameter_1 = 90
    result = grade_letter(parameter_1)
    expected = str   # Answer should be a string
    if type(result) != expected:
        print("Test case 5 failed. where the parameter", parameter_1, "output:", result, "instead of the expected:", expected, "as a string")






# Testing the function sort_students_into_grades():



# Test 1
def sort_students_into_grades_test1():
    argument = [{"name": "Hatem",
                 "grade": "A"},
                {"name": "Adam B",
                 "grade": "B"},
                {"name": "Adam C",
                 "grade": "C"},
                {"name": "Adam F",
                 "grade": "F"},
                {"name": "Adam Invalid",
                 "grade": "Invalid"},
                ]
    name = "Hatem"
    grade = "A"

    result = sort_students_into_grades(argument)
    result_list = result.get(grade)

    if result_list is not None:
        if name in result_list:
            return
        elif name not in result_list:
            print("Test case 1 failed.", name, "was not found on the list of students assigned the letter grade", grade + '.', "Instead the function returned", result)
    else:
        print("Test case 1 failed. The function did not return a dictionary with the key", grade + '.', "Instead the function returned", result)







sort_students_into_grades_test1()




#
#
# gcd_test1()
# gcd_test2()
# gcd_test3()
# gcd_test4()
# gcd_test5()
#
#
# replace_test1()
# replace_test2()
# replace_test3()
# replace_test4()
# replace_test5()
#
# grade_letter_test1()
# grade_letter_test2()
# grade_letter_test3()
# grade_letter_test4()
# grade_letter_test5()
#
#



# TODO Create test driver for whitebox tested functions
# TODO: Create test driver for blackbox tested functions
# TODO: Create test driver to test all functions

