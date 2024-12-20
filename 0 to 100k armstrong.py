for arms in range (1,100000):
    digit=0
    total=0
    numberx=arms
    while numberx>0:
        numberx=numberx//10
        digit +=1
    numberx= arms
    while arms>0:
         total += (arms%10)**digit
         arms=arms//10
    if total == numberx:
        print(numberx)


