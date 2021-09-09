"""
The Fibonaaci series is a sequence of positive integers where the following number
is the sum of the previous two numbers in the sequence.
"""

def FibonacciTerm(n):
    firstTerm = 0
    secondTerm = 1
    nextTerm = firstTerm + secondTerm

    i = 0
    while i < n:
        i = i + 1
        if i <= 2:
            continue

        nextTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = nextTerm
        
    return nextTerm

print("Get the nth term of the Fibonacci series.")

while True:
    print()
    try:
        n = int(input("Enter a positive integer greater than 2. Enter 0 to " +
                      "end this program\n"))
    except ValueError:
        print("You must enter a number")
        continue
    else:
        if n == 0:
            break
        if n <= 2:
           print("You must enter a positive integer greater than 1")
           continue
        term = FibonacciTerm(n)
        print("The number at position", n, "of the Fibonacci series is",
              str(term))

