build-docs:
	pdoc --html -o docs --force markowitz
	prettier --parser html --write docs/**.html
