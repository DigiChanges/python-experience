
down:
	@echo '************                               ************'
	@echo '************           DOWN CONTAINERS     ************'
	@echo '************                               ************'
	docker-compose down

dev:
	@echo '************                               ************'
	@echo '************           DEV INIT    	      ************'
	@echo '************                               ************'
	docker-compose up --build -d

up:
	@echo '************                               ************'
	@echo '************           UP Python    	      ************'
	@echo '************                               ************'
	uvicorn src.main:app --reload

exec:
	@echo '************                               ************'
	@echo '************           Exec NODE    	      ************'
	@echo '************                               ************'
	docker-compose exec node bash

init:
	@echo '************                               ************'
	@echo '************           Init NODE    	      ************'
	@echo '************                               ************'
	docker-compose exec node bash dev.init.sh

test:
	@echo '************                               ************'
	@echo '************           Test       	      ************'
	@echo '************                               ************'
	python -m pytest

clean:
	docker-compose down -v --remove-orphans
	docker ps -a | grep _run_ | awk '{print $$1}' | xargs -I {} docker rm {}
