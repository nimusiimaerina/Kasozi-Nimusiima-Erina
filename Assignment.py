#QUESTION1
print ("Hello, world! ")
print("Hello", "world!")
print (3) 
print(3.0)
print (2 + 3) 
print(2.0 + 3.0) 
print("2" + "3")
print( "2 + 3 =", 2 + 3) 
print(2 * 3)
print( 2**3 )
print(7/3)
print(7//3)

#QUESTION2
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x=3.9*x*(1-x)
        print(x)

main()

#QUETION3
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x=2.0*x*(1-x)
        print(x)

main()

#QUESTION4
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x=3.9*x*(1-x)
        print(x)

main()

#QUESTION5
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? ") ) 
    for i in range(n):
        x=3.9*x*(1-x)
        print(x)

main()

#QUESTION 6A
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x=3.9*x*(1-x)
        print(x)

main()
#QUESTION 6B
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x=3.9*(x-x*x)
        print(x)

main()

#QUESTION 6C 
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x=3.9*x-3.9*x*x
        print(x)

main()

#QUESTION 7
def main():
    print("This program illustrates a chaotic function")
    
    # Get two numbers from the user
    x1 = eval(input("Enter the first number between 0 and 1: "))
    x2 = eval(input("Enter the second number between 0 and 1: "))
    
    print("\nIteration\tValue 1\t\tValue 2")
    print("-" * 40)
    
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print(f"{i+1}\t\t{x1:.6f}\t{x2:.6f}")

main()

