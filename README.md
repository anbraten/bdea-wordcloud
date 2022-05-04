# bdea-workcloud

This project creates word-clouds based on tfidf for files which you can upload

## Project

### Team

* Anton Bracke
* Jan Mayer
* Julian Becker

### Documentation

- [docs/bdea_wordcloud.pdf](docs/bdea_wordcloud.pdf)
- [docs/demo_video.mp4](docs/demo_video.mp4)

## Demo

https://user-images.githubusercontent.com/6918444/166653958-757f2d0c-8b0a-4a5c-8674-830b359847ef.mp4

## Development

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/anbraten/bdea-wordcloud)

### Devcontainer

This project can be openend as [.devcontainer](https://code.visualstudio.com/docs/remote/containers) with VS-Code.

Continue with [Start backend / frontend](#start-backend--frontend)

### Local development (without devcontainer)

```bash
make docker-up
```

Open bash inside the app container with: `make docker-bash`

Continue with [Start backend / frontend](#start-backend--frontend)

### Start backend / frontend

```bash
make start # start webserver

make start-frontend # start frontend
```

## TODO
- [x] add frontend
- [x] add backend
- [x] add text file upload
- [x] generate wordcloud
- [x] embed wordcloud in frontend
- [x] add database to store document-frequiencies of words
- [x] add manual trigger for batch job to update document-frequiencies of words
