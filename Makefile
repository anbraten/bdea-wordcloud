MASTER := spark://spark:7077
DOCKER_COMPOSE := docker-compose -f .devcontainer/docker-compose.yml

.PHONY: all test coverage
all: get build install

wordcount: ## Run wordcount rdd
	spark-submit --master $(MASTER) --driver-class-path /poor-hdfs/postgresql-42.3.4.jar --jars /poor-hdfs/postgresql-42.3.4.jar spark/wordcount.py

docker-up: ## Start docker setup
	$(DOCKER_COMPOSE) up -d

docker-bash: ## Start bash on app service
	$(DOCKER_COMPOSE) exec app bash

postgres:
	$(DOCKER_COMPOSE) exec postgres psql -U postgres

start: ## Start the webserver
	FLASK_APP=src/server FLASK_ENV=development flask run --host=0.0.0.0

help: ## Display this help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
