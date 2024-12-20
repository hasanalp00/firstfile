numbery=int(input("say a squared number:"))
for rot in range (-numbery,1):
    square=rot**2
    if square==numbery:
        print (f"number's square root is {-rot}")
    else:
        continue