To run backend
 - uvicorn <app>:app --reload
To run frontend:
 - npm run start

Dockerize image:
 - docker build . -t <dockerFile>
 - docker run --rm --name backend --network foobar 8000:8000 backend
 - docker run --rm --name frontend --network foobar 3000:3000 frontend