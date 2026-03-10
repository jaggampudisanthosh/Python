n= int(input('Enter a number'))

last = n % 10

first = n
while first >= 10:
    first = first // 10

sum_digits = first + last

print(sum_digits)
