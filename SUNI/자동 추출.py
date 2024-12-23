import cv2
import pytesseract
import pyautogui
import numpy as np
import time
from collections import deque

# Tesseract-OCR 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kimhy\tesseract\tesseract.exe'

# 자막 추출 함수
def extract_subtitles():
    # 자막 영역의 좌표 설정 (x, y, width, height)
    x1, y1 = 311, 916
    x2, y2 = 1603, 986
    subtitle_region = (x1, y1, x2 - x1, y2 - y1)  # (x, y, width, height)

    previous_texts = deque(maxlen=5)  # 최근 5개의 텍스트 저장
    output_file = r'C:\Users\kimhy\Desktop\SUNI\subtitles.txt'

    time.sleep(3)  # 프로그램 시작 후 3초 대기

    while True:
        # 화면 캡처
        screenshot = pyautogui.screenshot(region=subtitle_region)
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # 이미지 전처리
        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환
        gray = cv2.GaussianBlur(gray, (5, 5), 0)  # 가우시안 블러로 노이즈 제거
        _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # 이진화

        # OCR로 텍스트 추출 (한글, 영어, 숫자 인식)
        custom_config = r'--oem 3 --psm 7'  # PSM을 7로 설정
        text = pytesseract.image_to_string(binary, lang='kor+eng', config=custom_config).strip()

        # 중복 텍스트 제거 및 파일에 저장
        if text and text not in previous_texts:  # 최근 텍스트와 비교
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(text + '\n')  # 텍스트 파일에 저장
            previous_texts.append(text)  # 현재 텍스트를 최근 텍스트에 추가

        time.sleep(1)  # 1초마다 캡처 (조정 가능)

try:
    extract_subtitles()
except KeyboardInterrupt:
    print("자막 추출을 중단합니다.")
