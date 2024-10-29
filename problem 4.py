"""
File 4 (problem4.py): 
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
"""

def fizzbuzz(n):
    answer = ""
    #Checks for the correct
    # range(start, stop, step) <- in this order
    for i in range(n, 0, -1):
        if ((n % 3 ==0) and (n % 5 == 0)):
            answer = answer + "FizzBuzz"
        elif i % 3 == 0:
            answer = answer + "Fizz"
        elif i % 5 == 0:
            answer = answer + "Buzz"
        else:
            answer = answer + str(i)
    #exit for loop
    return answer

#Testing ~
print("test one: " + fizzbuzz(6))

print("test two: " + fizzbuzz(42))

print("test tres: " + fizzbuzz(66))

print("test four: " + fizzbuzz(18))
