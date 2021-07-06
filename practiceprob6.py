from random import randint

a = int(input("Enter the lower bound: "))
b = int(input("Enter the upper bound: "))

# Generate some random integer
value1 = randint(a, b)
value2 = randint(a, b)
# print(value)
count1 = 0
count2 = 0
while True:
    print("Player 1:")
    m = int(input(f"Please guess the number between {a} and {b}: "))
    while True:
        if m == value1:
            count1 += 1
            break
        elif m > value1:
            count1 += 1
            m = int(input("Wrong guess! Enter a smaller number.. "))
        elif m < value1:
            count1 += 1
            m = int(input("Wrong guess! Enter a bigger number.. "))
    print("Player 2:")
    m = int(input(f"Please guess the number between {a} and {b}: "))
    while True:
        if m == value2:
            count2 += 1
            break
        elif m > value2:
            count2 += 1
            m = int(input("Wrong guess! Enter a smaller number.. "))
        elif m < value2:
            count2 += 1
            m = int(input("Wrong guess! Enter a bigger number.. "))

    break
print("Player 1 trails: ", count1)
print("Player 2 trials: ", count2)
if count1 > count2:
    print("Player 2 wins!!")
elif count1 == count2:
    print("Its a tie!!")
else:
    print("Player 1 wins!!")
