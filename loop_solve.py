# Loop problem-1: Counting Positive Numbers => solution

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
print("Positive numbers count: ", positive_number_count)

#Loop problem-2: Sum of Even Numbers => solution

n = int(input("Enter a number: "))

sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += 1
print("sum of even number: ", sum_even)

# Loop problem-3: Multiplication Table Printer => solution

numb = 4

for l in range(1, 11):
    if l == 5:
        continue
    print(numb, "*", l, "=", numb*l)