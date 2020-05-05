#Fibonacci sequence upto user specified number

a = int(input("Please enter a positive number: "))

def fn(n):
    x = 0
    y = 1
    
    print (x)
    print (y)

    for i in range(n):
        z = x +y
        x = y
        y = z
        print(z)

fn(a)
