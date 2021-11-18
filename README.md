# 기록

## 11월 17일 (수)

- 전체 계획 기획 및 웹 프로토 타입 제작
- 로그인, 회원가입 기능 구현
- api 사용하여 영화 데이터 가져오기
- erd 구현
- 영화 추천 알고리즘 탐구

## 11월 18일 (목)

- [ ] 모델 디자인 (accounts, community, movies)

[진행 상황](https://www.notion.so/68c0517a91bb46df871578d34769689b)

---

[타임라인](https://www.notion.so/81325ffc14f44b19aa3b66b03b996a9d)

---

[URL 기능](https://www.notion.so/09038c1510ba4048b4fddf25d783530a)

---

# 구현해야하는 기능들

### 관리자 뷰

- [ ] 관리자 권한의 유저만 영화 등록/수정/삭제 권한
- [ ] 관리자 권한의 유저만 유저 관리 권한을 가짐
- [ ] 장고 admin 기능을 이용하여 구현

### 영화 정보

- [ ] 최소 50개 이상의 데이터
- [ ] 모든 로그인 된 유저는 영화에 대한 평점/등록/삭제 등 가능

### 추천 알고리즘

- [ ] 평점을 등록한 유저는 해당 정보를 기반으로 영화를 추천 받을 수 있어야 한다
- [ ] 사용자는 반드시 최소 1개 이상의 방식으로 영화를 추천 받을 수 있어야 한다
- [ ] 어떠한 방식으로 추천 시스템을 구성했는지 설명

### 커뮤니티

- [ ] 영화 정보와 관련된 대화를 할 수 있는 커뮤니티 기능을 구현
- [ ] 로그인된 사용자만 글을 조회/생성할 수 있으며 작성자 본인만 글을 수정/삭제
- [ ] 사용자는 작성된 게시 글에 댓글을 작성할 수 있어야 하며, 작성자 본인만 댓글 삭제 가능
- [ ] 각 게시글 및 댓글은 생성 및 수정 시각 정보가 포함되어야 한다

### 기타

- [ ] 최소한 5개 이상의 URL 및 페이지를 구성
- [ ] HTTP Method와 상태 코드는 상황에 맞게 적절하게 반환되어야 하며, 필요에 따라 메시지 프레임워크 등을 사용하여 에러 페이지를 구성
- [ ] 필요한 경우 Ajax를 활용한 비동기 요청을 통해 사용자 경험을 향상 시켜야 한다

Front : Vue 

Back : Django

## 영화 추천 알고리즘

1. 평점, 인기도 기반 알고리즘 (가장 쉬움)
   $Weighted Rating (WR) = ( v / (v+m) * R)+(m / (v+m) * C)$
   v : 영화에 대한 평가 수
   m : 차트에 표시되어야 하는 최소 평가 수
   R : 영화의 평점
   C : 전체 영화에 대한 평균 점수
2. 오늘 월/일에 가까운 날짜, 계절에 개봉한 영화
3. 사용자 기반 알고리즘 (유저 데이터가 일정량 이상 쌓였을 때)
   - 좋아요한 영화의 장르와 같은 영화들 (ex:좋아요 10개 이상 일 때)