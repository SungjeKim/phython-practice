print("👋 안녕하세요! 저는 인사봇이에요. ('q'를 입력하면 종료됩니다.)")

while True:
    user_input = input("당신: ")

    if user_input == "q":
        print("👋 인사봇: 안녕히 가세요!")
        break
    elif "안녕" in user_input:
        print("인사봇: 안녕하세요! 반갑습니다 😊")
    elif "이름" in user_input:
        print("인사봇: 저는 인사 전문 챗봇이에요.")
    elif "날씨" in user_input:
        print("인사봇: 오늘 날씨가 정말 좋네요! ☀️")
    else:
        print("인사봇: 흠... 무슨 말인지 잘 모르겠어요 🤔")
