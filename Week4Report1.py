# 1. movie_rank 리스트 생성
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print("movie_rank = ",movie_rank)
# 2. 배트맨 추가
movie_rank.append("배트맨") 
print("movie_rank = ",movie_rank)
# 3. 슈퍼맨 추가 
movie_rank.insert(1, "슈퍼맨")
print("movie_rank = ",movie_rank)
# 4. 럭키 삭제
movie_rank.pop(3)
print("movie_rank = ",movie_rank)
# 5. 스플릿, 배트맨 삭제
movie_rank.pop()
movie_rank.pop()
print("movie_rank = ",movie_rank)
# 6. langs(lang1+lang2) 리스트 생성
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print("langs = ",langs)
# 7. 최대값, 최소값 출력
nums = [1,2,3,4,5,6,7]
print("max : ",max(nums))
print("min : ",min(nums))
# 8. 리스트의 합
nums2 = [1,2,3,4,5]
hap = 0
for i in range(len(nums2)):
    hap += nums2[i]
print("합계 : ",hap)
# 9. 리스트에 저장된 데이터 개수
cook = ["피자","깁밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print("개수 : ",len(cook))
# 10. 리스트의 평균
nums3 = [1,2,3,4,5]
hap = 0.0
for i in range(len(nums3)):
    hap += nums3[i]
print("평균 : ",hap/len(nums3))
