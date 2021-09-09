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
        i = i + 1 #we update the value of i here before anything else
        if i <= 2: #skip first and second term
            continue
    
        #reset the first, second and next term values
        nextTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = nextTerm
     
    #returns the last value of nextTerm
    return nextTerm

print("Get the nth term of the Fibonacci series.")

#we want this program to run for as long as the user wants
while True:
    print()
    try:
        n = int(input("Enter a positive integer greater than 2. Enter 0 to " +
                      "end this program\n"))
    except ValueError: #catch non-integer inputs
        print("You must enter a number")
        continue
    else:
        if n == 0: #end program here
            break
        if n <= 2: #handle call to first or second terms
           print("You must enter a positive integer greater than 1")
           continue
        #handle every other term
        term = FibonacciTerm(n)
        print("The number at position", n, "of the Fibonacci series is",
              str(term))

