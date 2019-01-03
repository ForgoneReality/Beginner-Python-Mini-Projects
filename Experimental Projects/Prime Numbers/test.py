from math import sqrt
#import os, sys

#PEP horror probably
def primes(number):
    """
    The algorithm for finding if a number is prime can be most efficiently solved by only going up to the square root of a number, rounded down
    That is because there this square root is the largest "pair" of two numbers multiplied together... if that makes sense.
    i.e. for 36, Finding the factor 2 will imply another factor x where x>6. The same is true for all other factors a<6 (3&12, 4&9).
    """
    for i in range(2, int(sqrt(number))+1):
        if number%i == 0:
            return False
    return True

def is_prime():
    """
    Practicing helper functions, could have been done within one.
    """
    cont = "y"
    while cont == "y" or cont == "Y":
        try:
            num = int(input("Please enter in a positive integer"))
            if num<=0:
                raise ValueError
        except ValueError:
            print("Input was not a positive integer")
        else:
            if primes(num):
                print("This is a prime number")
            else:
                print("This number is not prime")
        finally:
            cont = input("Continue? (y/n)");

is_prime()


"""
Below, I decided to test out the OS module which I just learned about. It has absolutely no relevance to the program itself.
"""

#print(os.getcwd()) #Starts with C:\Users\Charlie Xu\Testing, we want to rename this into \Beginner Python Projects
#print(os.listdir(os.getcwd()))
#os.mkdir(r"C:\Users\Charlie Xu\Beginner Python Projects")#Attempting to make a directory and transfer the current file (test.py) into it
#os.chdir(r"C:\Users\Charlie Xu\Beginner Python Projects")
#print(os.getcwd())
#print(os.listdir(os.getcwd()))
##Apparently, at this point the folder we just created remains empty.
    ##Changing our current working directory doesn't bring stuff from our old one, doh!

#os.rmdir(r"C:\Users\Charlie Xu\Beginner Python Projects") #Removed extraneous folder to make room for renaming

#os.rename(r"C:\Users\Charlie Xu\Testing", r"C:\Users\Charlie Xu\Beginner Python Projects")
"""
DOES NOT WORK! The current file and venv folder are open in the Pycharm IDE, which throws a WinError 32 when attempting to move.
To fix this issue, just move all these OS files to a separate folder and file, then we can move these files from there.
However, I'm too lazy to do that. I've played enough with the OS module to have a rudimentary idea of what it does, which was the purpose.
"""
#print(os.getcwd())
#print(os.listdir(os.getcwd()))