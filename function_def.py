import random

def print_track(h,t):
    for i in range(50):
        if h == t and h == i:
            print("@", end="")
        elif h == i:
            print("H", end="")
        elif t == i:
            print("T", end="")
        else:
            print("-", end="")
print()

def moveHare(a):
    x = random.randint(1,100)
    if x <= 10:
        a = a + 5
    elif x <= 30:
        a = a -1
    elif x <= 60:
        pass
    elif x <= 80:
        a= a + 1
    else:
        a = a + 2
    if a < 0:
        a = 0

    return a

def moveTortoise(a):
    x = random.randint(1,100)
    if x <= 25:
        a = a - 2
    elif x <= 60:
        pass
    elif x <= 85:
        a = a + 1
    else:
        a = a + 2
    if a < 0:
        a = 0

    return a
h = 0
t = 0
while h < 50 and t < 50:
    print_track(h, t)
    h = moveHare(h)
    t = moveTortoise(t)
    input()

    print("hare: ", h, "tortoise: ", t)

    if h > t:
        print("hare wins")
    elif h < t:
        print("tortoise wins")
    else:
        print("tie")