import random
ans = random.randint(1, 100)
upper, lower = 100, 1
guess = -1
print(f'{lower}~{upper}')
#重複比對直到答對
while guess != ans:
    guess = int(input())
    #(1)guess > ans
    if guess > ans:
        upper = guess
    #(2)guess < ans
    elif guess < ans:
        lower = guess
    #(3)guess == ans
    else:
        print('correct')
        break
    print(f'{lower}~{upper}')