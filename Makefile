build:
	@echo "Building Jupyter Book"
	jupyter-book build .

publish:
	@echo "Publishing Jupyter Book"
	ghp-import -n -p -f _build/html