# 1. print_reverse 함수 정의
def print_reverse(str):
    size = len(str)-1
    for i in range(size,-1,-1):
        print(str[i],end="")
print_reverse("python")
print("\n------1번 끝-------")
# 2. print_score 함수 정의
def print_score(scoreList):
    sum = 0.0
    for i in scoreList:
        sum += i
    print(sum/len(scoreList))
print_score([1,2,3])
print("------2번 끝-------")
# 3. print_even 함수 정의
def print_even(numList):
    for i in numList:
        if(i%2 == 0):
            print(i)
print_even([1,3,2,10,12,11,15])
print("------3번 끝-------")
# 4. calc_monthly_salary(annual_salary) 함수 정의
def calc_monthly_salary(annual_salary):
    annual_salary /= 12
    print(int(annual_salary))
calc_monthly_salary(12000000)
print("------4번 끝-------")
# 5. 코드 결과 예측(줄 바꿈은 무시했습니다)
def my_print(a, b):  # 예측 : 왼쪽: 200 오른쪽: 100
    print("왼쪽:", a) # 결과 : 왼쪽: 200 오른쪽: 100
    print("오른쪽:", b)
my_print(b=100,a=200)
print("------5번 끝-------")
# 6. 코드 결과 예측(줄 바꿈은 무시했습니다)
def 함수(num):      # 예측 : 22 
    return num + 4 # 결과 : 22
a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)
print("------6번 끝-------")
# 7. 코드 결과 예측(줄 바꿈은 무시했습니다)
def 함수(num):       # 예측 : 22
    return num + 4  # 결과 : 22
c = 함수(함수(함수(10)))
print(c)
print("------7번 끝-------")
# 8. 코드 결과 예측(줄 바꿈은 무시했습니다)
def 함수1(num):       # 예측 : 140
    return num + 4   # 결과 : 140
def 함수2(num):
    return num * 10
a = 함수1(10)
c = 함수2(a)
print(c)
print("------8번 끝-------")
# 9. 코드 결과 예측(줄 바꿈은 무시했습니다)
def 함수1(num):      # 예측 : 16 
    return num + 4  # 결과 : 16
def 함수2(num):
    num = num + 2
    return 함수1(num)
c = 함수2(10)
print(c)
print("------9번 끝-------")