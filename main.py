import os
from dotenv import load_dotenv
load_dotenv()

#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mastodon  # 터미널에 pip install Mastodon.py
import random  # 안깔아도 됩니다
from bs4 import BeautifulSoup  # 터미널에 pip3 install beautifulsoup4

def main():
    print('###### main 시작')

    # 봇으로 쓸 계정 키값 
    CLIENT_ID = 'dSxRhVTljZIFgtBI42MWy0Si0gSjlYotSKmipag38do'  # 클라이언트 키
    CLIENT_SECRET = '-jCbGZYGXEEGLeFZyRRW81q7FB56yBxMDSd5BpiQYkk'  # 클라이언트 비밀 키
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    BASE = os.getenv("BASE_URL")

    
    # 마스토돈 계정 인증!
    try:
        api = mastodon.Mastodon(
            client_id = CLIENT_ID,
            client_secret = CLIENT_SECRET,
            access_token = ACCESS_TOKEN,
            api_base_url = BASE)
        print('auth success')
    except Exception as e:
        print('auth fail')
        print(e)
    
    # 핸들러 시작
    handler = StreamHandler(api)
    api.stream_user(handler)

class StreamHandler(mastodon.StreamListener):
    def __init__(self, api):
        self.api = api

    def on_notification(self, notification):
        if notification["type"] == "mention":
            content = notification["status"]["content"]
            acct = notification["account"]["acct"]

            import re
            import html
            content = html.unescape(content)
            match = re.search(r"가챠/(\d+)회", content)
            if match:
                count = int(match.group(1))
                items = [
                    "안약", "꿀떡", "헤드셋", "착시현상 수영복", "신선한 초밥세트", "DVD 영화 묶음", "지퍼백", "우표가 수집된 앨범",
                    "노트", "클립", "QueeN Dream! 아이돌라이브 스타즈★ 블루레이 세트", "휴대용 망원경", "거대 심해어 인형", "우표",
                    "오선지", "신형 휴대용 게임기", "컴퓨터 부품", "허브 향초", "딸기 쇼트케이크", "만년필 잉크", "질 좋은 가죽 수첩", "감",
                    "CD 플레이어", "망가진 녹음기 인형", "로드 자전거 키링", "보드카", "유성 매직", "누군가의 결혼반지", "새 손수건", "적색 병잉크",
                    "토르티야", "생존키트", "행운의 편지", "기타 피크", "체스 도전장", "에너지 음료", "소라 껍질", "얼그레이 푸딩", "영화 포스터",
                    "스포츠 대회 영상이 담긴 USB", "팥죽", "기타 모양 키링", "연막탄", "안경닦이", "현금 다발", "유선 라벨지", "열심히 필기된 노트",
                    "하바리움", "손가락 골무", "지프차 카탈로그", "바퀴벌레 모형", "고급 물감", "조류 인형", "하○보 젤리 한 봉지",
                    "로렘이 표지 모델인 잡지", "목 베개", "종이학", "초콜릿 브라우니", "딸기잼 토스트", "질이 안 좋은 운동화", "로렘 인형", "소독약",
                    "4인 보드게임", "이단 성경", "생굴", "신발 덮개", "축축한 휴지 뭉치", "얼룩진 손수건", "향신료 선물 세트", "누군가의 운전면허 불합격 통지서",
                    "에너지바", "독약", "다 쓴 펜", "심령사진", "운동화", "담배", "일회용 접시", "사망보험 서류", "뉴스 아카이브 디스크", "무드등",
                    "위저보드", "주사기", "녹차 초콜릿", "민간요법 잡지", "오징어 회", "얇은 흰 장갑", "선수용 운동화", "필적을 알 수 없는 편지",
                    "무선 이어폰", "누군가의 박사 논문", "에너글리프 안경", "간장맛 사탕", "수취인 불명 편지", "협박 편지", "초보자도 할 수 있는 체스 기보 입문편",
                    "술", "타로카드", "절교장", "어느 예언가가 집필한 책", "야간 장식용 전구", "강령술 책", "붕대", "핫핑크색 네일팁", "무허가 건강보조식품",
                    "담배 꽁초", "돋보기", "병원비 고지서", "정체불명의 알약", "12색 볼펜", "누군가의 거절당한 러브레터", "화려한 목걸이", "우메보시", "레몬",
                    "다 끊어진 카세트테이프", "빳빳한 머리빗", "장난감", "스노우볼", "공룡화석", "녹음기", "코인 5개", "[꽝]"
                ]
                results = random.choices(items, k=count)
                response = f"도르륵... 아이템이 튀어나왔다. {results}"
                self.api.status_post(status=f"@{acct} {response}", in_reply_to_id=notification["status"]["id"])
if __name__ == "__main__":
    main()
