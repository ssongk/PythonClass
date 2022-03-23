import random

number1 = random.randint(1,100)
print("숫자를 맞혀 보세요. (1~100)")
userNum = int(input())

while 1:
    if number1 == userNum: 
        print("정답입니다. 입력한 숫자는",number1,"입니다.")
        break;
    elif number1 < userNum:
        print("숫자가 너무 큽니다.")
        userNum = int(input())
    elif number1 > userNum:
        print("숫자가 너무 작습니다.")
        userNum = int(input())