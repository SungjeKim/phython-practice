# 07_memo.py - 메모 저장 & 불러오기 통합 프로그램

print("====== 메모 프로그램 ======")
print("1. 메모 저장하기")
print("2. 저장된 메모 불러오기")
print("3. 프로그램 종료")

choice = input("원하는 작업의 번호를 선택하세요 (1~3): ")

if choice == "1":
    memo = input("저장할 메모를 입력하세요: ")
    with open("memo.txt", "w", encoding="utf-8") as file:
        file.write(memo)
    print("✅ 메모가 memo.txt에 저장되었습니다.")

elif choice == "2":
    try:
        with open("memo.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print("📄 저장된 메모 내용:")
            print(content)
    except FileNotFoundError:
        print("⚠️ 아직 저장된 메모가 없습니다. 먼저 저장해 주세요.")

elif choice == "3":
    print("👋 프로그램을 종료합니다.")

else:
    print("❌ 잘못된 입력입니다. 1~3번 중에서 선택해 주세요.")

