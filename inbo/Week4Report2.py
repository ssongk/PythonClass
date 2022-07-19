# 1. my_variable 빈튜플 생성
my_variable = ()
print("my_variable : ",my_variable)
# 2. movie_rank 튜플 생성
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print("movie_rank : ",movie_rank)
# 3. 숫자 1이 저장된 튜플 생성
numberOne = (1)
print("numberOne : ",numberOne)
# 4. 다음 코드 오류의 원인을 찾아라
# t = (1,2,3)
# t[0] = 'a' <- 튜플의 값은 수정할 수 없다
# 5. t가 바인딩하는 데이터 타입
t = 1,2,3,4
print("t의 타입 : ",type(t))
# 6. 튜플 수정
t2 = ("a","b","c")
t2 = list(t2)
t2[0] = "A"
t2 = tuple(t2)
print("t2 : ",t2)
# 7. 튜플 -> 리스트
interest = ("삼성전자", "LG전자", "SK Hynix")
interest = list(interest)
print("interest : ",interest)
# 8. 리스트 -> 튜플
interest = tuple(interest)
print("interest : ",interest)
# 9. 다음 코드의 실행 결과를 예상하라
temp = ("apple", "banana", "cake")
a, b, c = temp # 나의 예상 : a == b == c == "apple"
print(a, b, c) # 실제 결과 : a : apple, b : banana, c : cake
# 10. 1~99 중 짝수만 저장된 튜플 생성
even = []
for i in range(1,100):
    if i % 2 == 0:
        even.append(i)
even = tuple(even)
print("even = ",even)