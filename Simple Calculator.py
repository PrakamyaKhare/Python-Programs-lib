#simple clculator

str = 'ans = '

def add(a,b):
	c  = a + b
	print(str, c)
	
def subtract(a,b):
	c = a - b
	print(str,c)
	
def div(a,b):
	c = a/b
	print(str,c)	

def mul(a,b):
	c = a * b 
	print(str,c)

op = input("enter operator either + -  * or / ")
a = int(input("enter first operand "))
b = int(input("enter another operand "))

if  op == '+':
	add(a,b)
elif op == '-':
	subtract(a,b)
elif op == '*':
	mul(a,b)
elif op == '/':
	div(a,b)
