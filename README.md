# 인범이랑 진행하는 저장소


템플릿 후보
- https://startbootstrap.com/template-overviews/sb-admin-2/


주 계획 (8월 27일 기준 1주차)

예상 마감일 (10월 말)

1. 환경 설정 셋팅 및 타겟 사이트 조사
    - 아나콘다 및 각종 라이브러리 설치
    - vmware를 통한 centos 설치
    - python 설치
    - 깃허브 연동
    - 크롤링 파일 등 전달
    - 다음주 계획 논의
    - 회의 끝.

2. 크롤링 시작전 점검 및 크롤링 시작
    - 네이버 뉴스 및 타 사이트 크롤링 위험성
    - 데이터 저장 방법 논의
    
3. 크롤링 진행 중
    - 최대한 많은 데이터 수집
    - 정치, 경제, IT, 연예 4개 카테고리에서 진행
    - 6월 데이터부터 수집
    - 각 일자마다 50페이지 => 50x20x30 => 1달에 3만개 데이터 수집 예정
    - 6,7,8,9 => 12만개 데이터 수집

4. 데이터 전처리 방법
    - 단어 사전 구축
    - 개노가다
    
5. 프로그램 구체화 시작 예정
    - Django
    - keras(tensorflow)
        - RNN
        - CNN
    - NLP
    - word2vec
    - scikit-learn

** 중간 점검 18.10.12 기준 **
    1. 크롤러 수집 끝
    2-1. 단어 사전 구축 진행
    2-2. 형태소 분석 프로그램 구현 끝
    2-3. 단어 사전 구축시 자동으로 user dic 만들어주는 프로그램 구현 끝
    3. LSTM model training 테스트 끝
    4. tf-idf 테스트 끝
    5. word2vec 테스트 끝
    6. local vmware에 nginx, uwsgi 기반 django 서버 띄우기 성공
** 중간 점검 끝 **

6. 세부적 로직 구현
    - 장고 구현 -> 텍스트 받고 subprocess로 형태소 분석 python 파일 input 로직 구현
    - 형태소 분석 해주고 파일로 떨궈주는 프로그램 구현 => 문자열을 input으로 받는 로직은 짜놨음.
    - prediction 로직 구현
    - 형태소 분석 된 text와 tf-idf 단어장 비교해서 특징 단어 추출 로직 구현
    - 위에서 나온 단어를 word2vec에 넣어주는 로직 구현

7. 실제 시각화 구현(웹)
    - client input -> backend processing -> client output
    - word2vec visualization
    - client input sentences
    - tokenized word sentences
    - classification label output