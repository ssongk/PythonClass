time = int(input("최조 장비를 사용하기까지 걸린시간(초)를 입려하세요. "))

if time <= 60:
    print("생존율 : 85%")
elif time <= 120:
    print("생존율 : 76%")
elif time <= 180:
    print("생존율 : 66%")
elif time <= 240:
    print("생존율 : 57%")
elif time <= 300:
    print("생존율 : 47%")
elif time > 360:
    print("생존율 : 25% 미만")