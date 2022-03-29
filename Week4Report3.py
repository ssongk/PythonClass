# 1. inventory 딕셔너리 생성
inventory = {"메로나":[300,20],"비비빅":[400,3],"죠스바":[250,100]}
print("inventory = ",inventory)
# 2. 메로나 가격 출력
print("메로나 가격 : ",inventory["메로나"][0]," 원")
# 3. 메로나 재고 출력
print("메로나 재고 : ",inventory["메로나"][1]," 개")
# 4. inventory 딕셔너리에 데이터 추가
inventory["월드콘"] = [500,7]
print("inventory = ",inventory)
# 5. 딕셔너리의 key 값만 추출해 리스트 구성
icecream = {"탱크보이":1200,"폴라포":1200,"빵빠레":1800,"월드콘":1500,"메로나":1000}
icecreamKeys = icecream.keys()
print("icecreamKeys = ", icecreamKeys)
# 6. 딕셔너리의 value 값만 추출해 리스트 생성
icecreamValues = icecream.values()
print("icecreamValues = ", icecreamValues)
# 7. 아이스크림 판매 금액의 총합 구하기
hap = 0
for i in icecream:
    hap += icecream[i]
print("합계 : ",hap)