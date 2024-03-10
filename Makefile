build:
	@echo "Building Jupyter Book"
	jupyter-book build .

build-pdf:
	@echo "Building Jupyter Book PDF"
	jupyter-book build . --builder pdfhtml

publish:
	@echo "Publishing Jupyter Book"
	ghp-import -n -p -f _build/html