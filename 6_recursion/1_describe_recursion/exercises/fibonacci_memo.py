#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Use test cases, the docstring, and labels to describe this solution. """


def fibonacci(n: int, memo: dict = {}) -> int:
    """
    Returns the value item number n of the Fibonacci list

    base case 1: 
     0 returns 0
    
    base case 2:
     1 returns 1
     
    base case 3:
     n is in memo returns value from memo
     
    recursive case:
    n isn't in memo and >1 returns f(n-1)+f(n-2)
    """
<<<<<<< HEAD
    
    if n == 0: # base case 1
        return 0 # turn-around 1

    if n == 1: # base case 2
        return 1 # turn-around 2

    if n in memo: # base case 3
        return memo[n] # turn around 3
    
    # recursion 1 | break down 1
    left_recursion = fibonacci(n - 1, memo)
    
    # recursion 2 | break down 2 
    right_recursion = fibonacci(n - 2, memo)
    
    # build-up
=======
    if n == 0: #
        return 0 #

    if n == 1: #
        return 1 #

    if n in memo: #
        return memo[n] #
    
    # 
    left_recursion = fibonacci(n - 1, memo)
    # 
    right_recursion = fibonacci(n - 2, memo)
    # 
>>>>>>> 618f7e71d2be245c047cd7ddd40361da80165564
    memo[n] = left_recursion + right_recursion
    
    return memo[n]


# --- --- --- test cases --- --- ---

print (fibonacci(0)," should be ", 0) #base case 1
print (fibonacci(1)," should be ", 1) #base case 2
print (fibonacci(3),' should be ', 2)
print (fibonacci(4),' should be ', 3)
print (fibonacci(5),' should be ', 5)
print (fibonacci(10),' should be ', 55)
