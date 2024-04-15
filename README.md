# Sparta-Project-
스파르타 마켓


## 🖥️ 프로젝트 소개
게시글과 댓글 CRUD를 구현한 홈페이지입니다.

ERD : 
[SpartaMarket_ERD.pdf](https://github.com/HyunHyoMin/spartamarket/files/14975149/SpartaMarket_ERD.pdf)


## 🕰️ 개발 기간
* 24.04.12. - 24.04.19. / 8일

### ⚙️ 개발 환경
- Backend : `Python`
- Frontend : `HTML, CSS, JavaScript`
- **Framework** : Django
- **Database** : SQLite

## 📌 주요 기능
#### 회원가입
- ID 중복 체크
- PW 일치하는지 확인
- ID 형식과 PW 형식이 일치하는지 확인
#### 로그인
- Id, PW가 DB에 있는지 확인
- 로그인 시 세션(Session) 생성
- 로그인 시 메인 페이지에 로그인한 Id의 닉네임 표시
- 로그인 시 게시글과 댓글 작성 가능
#### 관리자 계정
- DB에 자동 생성
- ID : admin / PW : admin
- 모든 게시글과 댓글 수정, 삭제 가능
#### 게시글
- 글 작성, 읽기, 수정, 삭제(CRUD)
- 글을 작성한 계정만 수정, 삭제 가능
- 글 작성 시 작성한 Id의 닉네임, 제목, 내용, 작성한 날짜와 시간 표시
- 메인페이지에서 게시글 제목/작성자/내용에 따라 검색 가능(검색어가 포함된 모든 게시글 조회)
#### 댓글
- 댓글 작성, 읽기, 수정, 삭제(CRUD)
- 댓글 작성 시 작성한 Id의 닉네임, 제목, 내용, 작성한 날짜와 시간 표시
- 댓글을 작성한 계정만 수정, 삭제 가능
