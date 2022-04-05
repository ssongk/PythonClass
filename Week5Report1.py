# 1. 코드 결과 예측(줄 바꿈은 무시했습니다)
def message1(): # 예측 : A B C A B
    print("A")  # 결과 : A B C A B
    print("B")
message1()
print("C") 
message1()
print("-----1번 끝-----")
# 2. 코드 결과 예측(줄 바꿈은 무시했습니다)
print("A")
def message2(): # 예측 : A C B
    print("B")  # 결과 : A C B
print("C") 
message2() 
print("-----2번 끝-----")
# 3. 코드 결과 예측(줄 바꿈은 무시했습니다)
print("A")
def message3_1(): # 예측 : A C B E D
    print("B")    # 결과 : A C B E D
print("C")
def message3_2():
    print("D")
message3_1()
print("E")
message3_2()
print("-----3번 끝-----")
# 4. 코드 결과 예측(줄 바꿈은 무시했습니다)
def message4_1(): # 예측 : B A
    print("A")    # 결과 : B A
def message4_2():
    print("B")
    message4_1()
message4_2()
print("-----4번 끝-----")
# 5. 코드 결과 예측(줄 바꿈은 무시했습니다)
def message5_1(): # 예측 : B C B C B C A
    print("A")    # 결과 : B C B C B C A
def message5_2():
    print("B")
def message5_3():
    for i in range(3):
        message5_2()
        print("C")
    message5_1()
message5_3()
print("-----5번 끝-----")
# 6. print_arithmetic_operation 함수 작성
def print_arithmetic_operation(a,b):
    print("a + b =",a+b)
    print("a - b =",a-b)
    print("a * b =",a*b)
    print("a / b =",a/b)
print_arithmetic_operation(3, 4)
print("-----6번 끝-----")
# 7. print_max 함수 정의
def print_max(a,b,c):
    if(a>b):
        if(a>c):
            print("max는",a)
        elif(a<c):
            print("max는",c)
    elif(b>a):
        if(b>c):
            print("max는",b)
        elif(b<c):
            print("max는",c)
A = input("첫 번쨰 수자 입력>>")
B = input("두 번쨰 수자 입력>>")
C = input("세 번쨰 수자 입력>>")
print_max(A,B,C)
print("-----7번 끝-----")