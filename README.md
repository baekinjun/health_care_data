# health_care_data

1.healthcare 의 데이터를 다루는 flask api서버입니다.

## INSTALLATION
How to install source code:


    git clone https://github.com/baekinjun/health_care_data.git

    
## RUN
how to run this flask api server:

    docker-compose up -d --build
    
    
## apidocs confirm
using flasgger (swagger lib)

    localhost or your ip address
    ex) localhost/apidocs
    
<img width="1053" alt="스크린샷 2021-05-23 오후 10 23 46" src="https://user-images.githubusercontent.com/58027908/119262271-92e8d680-bc15-11eb-853b-05d25fd26f24.png">

    
## 구현하면서 생각
1. 해당 데이터들을 확인 하여 파악
2. 어떤 아키텍처와 디자인 패턴을 사용할지 선정
3. 해당 아키텍처에 대해 필요한 라이브러리 들을 선정 
4. 코드 구현
5. apidocs swagger 정리하여 쉽게 api를 쉽게 확인할수있도록 정리
