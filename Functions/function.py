# All Answers are down below


# 1. Basic Function Syntax => solution

def square_num(c):
    square = c ** 2
    print(square)
    return square

square_num(5)
square_num(2)
square_num(10)
# result = square_num(5)
# print(result)


# 2. Function with Multiple Parameters => solution

def add(j, a):
    sumation = j + a
    print(sumation)
    return sumation

add(4, 5)
add(13, 29)

# 3.  Polymorphism in Functions => solution

def multiply(c1, c2):
    m = c1 * c2
    print(m)
    return m 

multiply(6, 11)
multiply(6, "hi")

# 4. Function Returning Multiple Values => solution

def circle_stat(radius):
    area = 3.14 * (radius ** 2)
    circumference = 2 * 3.14 * radius
    print(area, circumference)
    return area, circumference

circle_stat(3)

# 5.  Default Parameter Value => solution

def greeting(name = "Jawad"):
    greet = "Assalamualikum, " + name
    print(greet)
    return greet

greeting('Ahona')

# 6. Lambda Function => solution

# def cubic(a):
#     return a ** 3

cube = lambda d: d ** 3

print(cube(4))

# 7. Function with *args => solution

def sum_all(*args):
    return sum(args)

print(sum_all(2, 4, 5))
print(sum_all(4, 8, 3, 3, 6))
print(sum_all(20, 40, 78))

# 8. Function with **kwargs => solutiom

def team_play(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

team_play(team="Barca", player="Messi", Goalkeeper="Stegan")
team_play(team="Madrid", player="Ronaldo")
team_play(team="Hilal", player="Neymar", Goalkeeper="Yussof")

# 9. Generator Function with yield => solution

def yield_sol(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in yield_sol(14):
    print(num)


# 10. Recursive Function => solution

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    