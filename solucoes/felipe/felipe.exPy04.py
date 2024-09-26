#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:31:13 2019

@author: felipe

ex 04 
"""

# %% 1.

# Write a function that returns the maximum of two numbers

def mmax(a, b):
    return a if a > b else b    

# %% 2.
"""
    Write a function called fizz_buzz that takes a number.

    If the number is divisible by 3, it should return “Fizz”.
    If it is divisible by 5, it should return “Buzz”.
    If it is divisible by both 3 and 5, it should return “FizzBuzz”.
    Otherwise, it should return the same number.
"""

def fizz_buzz(n):
    if n % 5 == 0 and n % 3 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    #default:
    return str(n)
    
# %%    
    
"""
Write a function for checking the speed of drivers. This function should have one parameter: speed.

    If speed is less than 70, it should print “Ok”.
    Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
    If the driver gets more than 12 points, the function should print: “License suspended”
"""
points =0 

def drivers(speed):
    global points
    
    if speed <= 70:
        print "ok"
    if speed > 70:
        print"infraçao"
        points+=1
        print points
    if points>12:
        print "license suspended"
        

 # %%
 
"""
 Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:

    0 EVEN
    1 ODD
    2 EVEN
    3 ODD
    
"""

def showNumbers(limit):
    for x in range(0,limit):
        if x % 2 == 0:
            print x, "EVEN"
        else:
            print x, "ODD"
    
# %%        

# Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

def mul35(limit):
    for x in range(0,limit):
        if x % 5 == 0 or x % 3 == 0 :
            print x

# %%

"""
Write a function called show_stars(rows). 
If rows is 5, it should print the following: 
"""

def show_start(rows):
    st = "*"
    for x in range(rows):
        
        print st
        st+="*"

# %%

"""
Write a function that prints all the prime numbers between 0 and limit 
where limit is a parameter.
"""

def primos(limit):
    isprimo = True
    for i in range(2,limit):
        if limit % i==0:
            isprimo = False
    return isprimo
                
                
        
        
    