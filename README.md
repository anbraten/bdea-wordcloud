# bdea-workcloud


Geh zu .devcontainer:

``` docker-compose build
docker-compose up -d
docker-compose exec app bash
```
In der container app:
```
make wordcount
make start
``` 

## TODO
- [ ] add frontend
- [x] add backend
- [ ] add text file upload
- [ ] trigger wordcount with spark after file upload
- [x] generate wordcloud
- [ ] embed wordcloud in frontend
- [ ] add manual trigger for document word count