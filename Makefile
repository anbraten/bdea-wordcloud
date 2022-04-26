MASTER := spark://spark:7077

.PHONY: all test coverage
all: get build install

wordcount: ## Run wordcount rdd
	spark-submit --master $(MASTER) src/wordcount.py

start:
	FLASK_APP=src/server FLASK_ENV=development flask run

help: ## Display this help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
