run:
	python3 src/main.py

clean:
	rm -rf src/components/__pycache__
	rm -rf .DS_Store

test:
	python3 tests.py
