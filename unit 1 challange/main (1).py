n = int(input("enter number whose factorial is required : "))
factorial = 1
i = 1
while i <= n:
  factorial = factorial * i
  i = i + 1
  print('factorial of', str(n) + 'is', str(factorial))
