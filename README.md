# bdea-workcloud

##Team
* 2211663 - Anton Bracke
* 2210897 - Jan Mayer
* 1911034 - Julian Becker

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/anbraten/bdea-wordcloud)

https://user-images.githubusercontent.com/6918444/166653958-757f2d0c-8b0a-4a5c-8674-830b359847ef.mp4

## Devcontainer

This project can be openend as [.devcontainer](https://code.visualstudio.com/docs/remote/containers) with VS-Code.

## Local development (without devcontainer)

```bash
cd .devcontainer/

docker-compose build
docker-compose up -d
docker-compose exec app bash
```


Inside the app container:

```bash
make wordcount # run batch job in spark
make start # start webserver
``` 

Inside `frontend/`:
```bash
npm install # install dependencies 
npm run dev  # starts development server
npm run build # builds frontend for production in src/templates
```

## TODO
- [x] add frontend
- [x] add backend
- [x] add text file upload
- [x] generate wordcloud
- [x] embed wordcloud in frontend
- [x] add database to store document-frequiencies of words
- [x] add manual trigger for batch job to update document-frequiencies of words
