# for loop
"""for i in range(1, 11):
    num = i*i
    print(num)
    
    if num == 36:
        print("found")
        break
        
n = 5
for i in range(n):
    for j in range(n-i):
        print("*",end=' ')
    print()    
    
n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print()     

n = 5
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()     
    
n = 5
for i in range(n):
    for j in range(n-i):
        print(" ",end='')
    for j in range(i+1):
        print("*",end=' ')    
    print()  
    
    
n1 = int(input("enter number"))      
for n1 in range (1,n1+1):
    print(n1)
     
total = 0     
n2 = int(input("enterhow many numbers added"))      
for n2 in range (1,n2+1):
    numbers = int(input("enter numbers"))
    total = total + numbers
    print("sum=",total)


n = int(input("enter a number"))
number = len(str(abs(n)))
print(number)
if n == 0:
    count = 1
    print(count)
else:
    count = 0
    n = abs(n)
while n > 0:
    count +=1
    n//=10
print(count)"""

n = int(input("Enter a number: "))

temp = abs(n)      # store original number (positive)
rev = 0

while temp > 0:
    digit = temp % 10        # get last digit
    rev = rev * 10 + digit  # build reverse number
    temp //= 10             # remove last digit

if abs(n) == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

