install:
	pip3 install -r requirements.txt
	python -m venv venv2

run:
	cls && .\venv2\Scripts\activate && python pre_main.py && python main.py


poc:
	nodemon -e "*.py" --exec "python poc.py"