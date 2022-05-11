# bdea-workcloud

This project creates word-clouds based on a tfidf calculation for txt-files which you can upload via a web-UI by using a spark cluster with pyspark.

## Project

### Team

* Anton Bracke
* Jan Mayer
* Julian Becker

### Documentation

[docs/bdea_wordcloud.pdf](docs/bdea_wordcloud.pdf)

[docs/presentation.pdf](docs/presentation.pdf)

[![YouTube Demo Video](https://img.youtube.com/vi/Z8s7Z4lzZ6U/0.jpg)](https://youtu.be/Z8s7Z4lzZ6U)

## Content

- Spark jobs: [spark/](spark/)
- Frontend: [frontend/](frontend/)
- Backend: [backend/](backend/)
- Fake HDFS: [fake-hdfs/](fake-hdfs/)

## Development

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/anbraten/bdea-wordcloud)

### Devcontainer

This project can be openend as [.devcontainer](https://code.visualstudio.com/docs/remote/containers) with VS-Code.

Continue with [Start backend / frontend](#start-backend--frontend)

### Local development (without devcontainer)

```bash
make docker-up
```

Open a bash inside the app container with: `make docker-bash`

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
