import random

def compareNumber(userNumCopy,comNumCopy):
    strikeCount = 0
    ballCount = 0
    userNumCount = 0
    comNumCount = 0
    
    for i in range(3):
        for j in range(3):
            if(userNumCopy[i]==comNumCopy[j]):
                if(i==j):
                    strikeCount += 1
                else:
                    ballCount += 1
    print(strikeCount,"스트라이크",ballCount,"볼")
    return strikeCount

strike = 0
comNum = 0
while(1):
    for k in range(3):
        comNum += random.randint(1,9) * 10 ** k
    print("답 :",comNum)
    comNum = str(comNum)
    if(comNum[0]!=comNum[1] and comNum[0]!=comNum[2] and comNum[1]!=comNum[2]):
        break
    else :
        continue

while(strike!=3):
    userNum = input("세자리 숫자 입력>>")
    strike = compareNumber(userNum,comNum)