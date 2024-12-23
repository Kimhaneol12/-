import pyautogui

# 현재 마우스 위치 출력
try:
    print("마우스를 원하는 위치에 두고 Enter 키를 누르세요...")
    input()  # 사용자 입력 대기
    position = pyautogui.position()
    print(f"현재 마우스 위치: {position}")  # 마우스 위치 출력
except KeyboardInterrupt:
    print("프로그램을 종료합니다.")
    
