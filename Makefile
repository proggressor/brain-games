install: #развёртвыем poetry
	poetry install

brain-games: #запуск brain-games
	poetry run brain-games

build: #сборка пакета
	poetry build

publish: #публикация пакета
	poetry publish --dry-run

package-install: #установка пакета из ОС
	python3 -m pip install dist/*.whl --force-reinstall
	
lint: #запуск линтера
	poetry run flake8 brain_games
	