DOCKER_SPARK := docker-compose exec pyspark
MASTER := spark://spark:7077

.PHONY: all test coverage
all: get build install

up: ## Build and run docker setup
	@docker-compose up -d

count: ## Run count example
	$(DOCKER_SPARK) spark-submit --master $(MASTER) count.py

help: ## Display this help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
