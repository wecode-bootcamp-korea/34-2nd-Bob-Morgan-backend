# Bob Morgan (위코드 34기 2차 프로젝트)

<img width="788" alt="Screen Shot 2022-07-15 at 4 14 49 PM" src="https://user-images.githubusercontent.com/102043891/179171989-8c2b0230-bcc9-4f1f-8958-e1d6a7da1463.png">

- 기존의 [카모아 사이트](https://carmore.kr/home/index.html?)는 렌터카 비교, 예약 사이트입니다.
- 저희 팀은 차가 아닌 맛집으로 변경하여 제주도 맛집 검색/예약 사이트를 기획하였습니다.

<br><br>

## 🎙 설명

위의 레포지토리는 [위코드 부트캠프](https://github.com/wecode-bootcamp-korea)의 [34기 백엔드 2차 프로젝트](https://github.com/wecode-bootcamp-korea/34-2nd-Bob-Morgan-backend)입니다.

- [Watcha Classic 백엔드 GitHub 링크](https://github.com/wecode-bootcamp-korea/34-2nd-Bob-Morgan-backend)
- [Watcha Classic 프론트엔드 GitHub 링크](https://github.com/wecode-bootcamp-korea/34-2nd-Bob-Morgan-frontend)

<br><br>

## 📆 개발 기간
- 개발 기간 : 2022-07-04 ~ 2022-07-15 (11일)

<br><br>

## 🧑🏻‍💻 팀 구성원
- Backend : 이태권(PM)
- Frontend: 박수연, 이범석, 이후경, 정예지
<br><br>

## 🖥 Backend 역할

**[이태권(PM)](https://github.com/dev-taekwonlee)**
- dbdiagram을 이용한 모델링
- ERD를 실제 model에 적용
- csv file to MySQL
- 카카오 로그인 구현 `signin/kakao`
    - FE가 kakao에서 발급 받은 access token을 받아 서비스의 자체적인 토큰 발급 `GET`
- signin decorator 구현
- 메인 페이지  API 구현 `GET`
- 검색 페이지 `PlaceSearchView` API 구현 `GET`
- 상세 페이지 `PlaceDetailView` API 구현 `GET`
- 예약 기능 `PlaceReservationView` API 구현 `POST`

<br><br>

## 💻 Backend 기술 스택

|                                                Language                                                |                                                Framwork                                                |                                               Database                                               |                                                     ENV                                                      |                                                   HTTP                                                   |
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=black"> | <img src="https://img.shields.io/badge/miniconda3-44A833?style=for-the-badge&logo=anaconda&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |

<br>
<br>


<br>
<br>

## 📚 팀 프로젝트 자료

### ERD

![bob_morgan_db_20220707_1700](https://user-images.githubusercontent.com/102043891/179173551-cc887023-1919-4fcf-a9a6-36edf824775d.png)

<br>

### 사이트 시현 사진
<img width="1056" alt="Screen Shot 2022-07-16 at 5 57 57 AM" src="https://user-images.githubusercontent.com/102043891/179309787-1cf9402c-8369-4868-baba-e0158b92d17b.png">

<br>

### 사이트 시현 영상
[데모 영상](https://youtu.be/nHldPtd5YDU)

<br>
<br>


## 🛠 협업 툴

### Slack
- 팀원들과의 자료 공유 및 개인적 소통
<img width="857" alt="Screen Shot 2022-07-15 at 9 54 05 AM" src="https://user-images.githubusercontent.com/102043891/179173787-e68a0558-f46d-4680-9da0-c8d8bf035fed.png">

### Notion
- 주로 회의록으로 이용
- 매일 진행되는 stand-up meeting에서 각자의 진행 상황과 Blocker 파악 및 소통
<img width="787" alt="Screen Shot 2022-07-16 at 8 30 54 AM" src="https://user-images.githubusercontent.com/102043891/179324213-e9563579-8699-40b5-9b72-43457ed79787.png">
- 매주 월요일에 진행되는 sprint meeting을 통해 필수 기능 구현과 추가 기능 구현을 명확히 구분 및 조정
<img width="667" alt="Screen Shot 2022-07-15 at 1 46 53 AM" src="https://user-images.githubusercontent.com/102043891/179173829-1130b713-a6d5-43ff-9329-cca941822ad0.png">


### Trello
- stand-up meeting을 마친 후 각자 Trello에 반영하여 작업 현황을 일목요연하게 공유
<img width="1064" alt="Screen Shot 2022-07-16 at 6 19 53 AM" src="https://user-images.githubusercontent.com/102043891/179324134-ed4a983a-ea8d-4fca-80ec-455da379a41f.png">

<br>
<br>

## 🔖 Reference
- 이 프로젝트는 [카모아 사이트](https://carmore.kr/home/index.html?) 사이트를 참조하여 학습 목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습 용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
