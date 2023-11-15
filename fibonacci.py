# recursive 

def Fibonacci(n):
	if n<= 0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n == 1:
		return 0
	# Second Fibonacci number is 1
	elif n == 2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(10))

#non recursive

def fibonacci_iterative(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

n=10
result_iterative=fibonacci_iterative(n)
print("The Fibonacci number is:", result_iterative)       
