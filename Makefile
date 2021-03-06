help:
	echo "OPTIONS: authenticate, run, version, parameter_test, test"

authenticate:
	python3 ./src/GetAuthentication.py

run:
	python3 ./src/PyPocket.py --verbose --tagSearch="export emacs" --removeTag

version:
	python3 ./src/PyPocket.py --version

parameters_test:
	python3 ./src/PyPocket.py --debug --tagSearch="export emacs" --doNotSave

test:
	cd ./test && python3 -m unittest -v

.PHONY: test clean