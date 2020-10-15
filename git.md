# 프로젝트에서 사용할 git 규칙

## branch

- master (배포서버 올릴거 종합)



- develop (feature 종합 + 필요시 배포 전 테스트)


**feature는 최신 develop 브랜치에서 생성합시다**
- feature/login (feature 브랜치, / 뒤에 feature 이름 붙이기)
  - feature/login-jw (- 뒤에 작업자 이름 이니셜 붙이기)
  - feature/login-js
  - ...
- feature/{feature_name} 
  - ...

- feature 이름에 띄어쓰기는 `_`를 사용합시다.
  - ex) `feature/django_init`



## Commit

- 길게 적을일 없을 것 같아서 git commit -m 옵션으로 작성합시다.
- 한번에 서로 다른 작업 수정했을 경우 가능하면 add를 따로 해서 커밋합시다.
- 커밋 메세지는 jira 이슈와 `|` 를 사용해 스마트커밋 합시다.
  - ex) `S03P23D105-47 | fix main display bug`



## Tip

- pull 받기 전 변경사항 때문에 conflict 난 경우는 stash를 써보세요.
  - [참고링크](https://gmlwjd9405.github.io/2018/05/18/git-stash.html)

