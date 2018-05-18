authenticate:
	python3 ./src/GetAuthentication.py

run:
	python3 ./src/PyPocket.py

test:
	cd ./test && python3 -m unittest -v

.PHONY: test clean