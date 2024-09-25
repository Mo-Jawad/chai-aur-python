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

#Loop problem-4: Reverse a String => solution

text = "Jawad"
reverse_text = ""

for char in text:
    reverse_text = char + reverse_text
print(reverse_text)

#Loop problem-5: Find the First Non-Repeated Character => solution

word = "Nooppeec"

for w in word:
    if word.count(w) == 1:
        print("non-repeated char: ", w)
        break

#Loop problem-6: Factorial Calculator => solution

pick = 7
factorial = 1

while pick >= 1:
    # factorial = factorial * pick
    # pick = pick - 1
    factorial *= pick
    pick -= 1
print("The factorial value is: ", factorial)

# Loop problem-7: Validate Input => solution

while True:
    P = int(input("Enter b/w 1 to 10: "))

    if 1 <= P <= 10:
        print("Thanks")
        break
    else:
        print("invalid, try again")
        
    # break

# Loop problem-8: Prime Number Checker => solution

N = int(input("enter a number: "))

is_prime = True

if N > 1:
    for i in range(2, N):
        if (N % i) == 0:
            is_prime = False

print("Prime: ",is_prime)

# Loop problem-9: List Uniqueness Checker => solution

items = ["apple", "banana", "orange", "apple", "mango", "orange"]

duplicate_items = set()

for item in items:
    if item in duplicate_items:
        print("duplicate: ", item)
        break
    duplicate_items.add(item)


# Loop problem-10: Exponential Backoff => Solution

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("attempt", attempts + 1, "- wait time", wait_time)
    # wait_time = wait_time * 2
    wait_time *= 2
    attempts += 1
    time.sleep(wait_time)
    