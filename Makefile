.PHONY: all $(MAKECMDGOALS)

# Agrego un comentario al Makefile
run:
	docker run --rm --volume `pwd`:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py words.txt yes