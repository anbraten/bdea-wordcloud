# bdea-workcloud

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/anbraten/bdea-wordcloud)

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

## TODO
- [ ] add frontend
- [x] add backend
- [x] add text file upload
- [x] generate wordcloud
- [x] embed wordcloud in frontend
- [ ] add database to store document-frequiencies of words
- [ ] add manual trigger for batch job to update document-frequiencies of words
