# health_care_data

1.healthcare 의 데이터를 다루는 flask api서버입니다.

## INSTALLATION
How to install source code:


    git clone https://github.com/baekinjun/health_care_data.git

    
## RUN
how to run this flask api server:
 보내드린 config.yaml 파일을 healthcare/config/ 밑으로 붙여넣고 아래 코드를 실행합니다.

    docker-compose up -d --build
    
    
## apidocs confirm
using flasgger (swagger lib)

    localhost or your ip address
    ex) localhost/apidocs
    
<img width="1053" alt="스크린샷 2021-05-23 오후 10 23 46" src="https://user-images.githubusercontent.com/58027908/119262271-92e8d680-bc15-11eb-853b-05d25fd26f24.png">

    
## 문제를 어떻게 풀었는지 우선순위
1. 해당 데이터들을 확인 하여 파악
2. 어떤 아키텍처와 디자인 패턴을 사용할지 선정
3. 해당 아키텍처에 대해 필요한 라이브러리 들을 선정 
4. 코드 구현
5. apidocs swagger 정리하여 쉽게 api를 쉽게 확인할수있도록 정리

## 이후 해나가야할것
1. 검색쪽의 데이터가 많아서 es 를 사용하면 훨씬 빠르게 검색 엔진을 구축할수 있을것 같습니다.
2. 데이터에 대해 조금더 명확히 이해를 하면 구현하는대 좀더 질좋게 만들수 있을것 같습니다.
3. orm을 사용하여 조금더 쉽게 페이지네이션을 구현할수 있습니다.
