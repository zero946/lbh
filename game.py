print("게임을 시작합니다")
print("테트리스 시작")
print("1. 오른쪽 2. 왼쪽 3. 바꾸기")
while 1:
    number = input("숫자를 입력하세요: ")
    print("당신이 입력한 숫자는?", number)
    if int(number) == 1:
        print("오른쪽으로 이동")
    if int(number) == 2:
        print("왼쪽으로 이동")
    if int(number) == 3:
        print("바꾸기")
    if int(number) == 0:
        print("게임종료")
        break


