useElec = float(input("전기 사용량을 입력하세요. "))

print("사용량 :", useElec, "kwh")
if useElec <= 200:
    print("기본요금 : 910 원")
    print("단가 : 99.3 원")
    print("전기 요금 :", useElec*910, "원")
elif useElec <= 400:
    print("기본요금 : 1600 원")
    print("단가 : 187.9 원")
    print("전기 요금 :", useElec*1600, "원")
elif useElec > 400:
    print("기본요금 : 7300 원")
    print("단가 : 280.6 원")
    print("전기 요금 :", useElec*7300, "원")