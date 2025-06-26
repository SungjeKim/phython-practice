# 1부터 5까지 숫자 출력
for i in range(1, 6):
    print(i)

# 과일 리스트 반복 출력
fruits = ["사과", "바나나", "딸기", "포도"]

for fruit in fruits:
    print("과일:", fruit)

# 1부터 5까지 출력 (while)
i = 1
while i <= 5:
    print(i)
    i += 1
for i in range(1, 11):
    if i % 2 == 0:
        print("짝수:", i)

while True:
    text = input("아무 말이나 입력하세요 (끝내려면 q 입력): ")
    if text == "q":
        print("프로그램을 종료합니다.")
        break
    print("입력한 내용:", text)

