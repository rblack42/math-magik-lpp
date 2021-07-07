.PHONY: pyinit
pyinit:	## Create Python virtual environment
	test -d .direnv || \
	echo 'layout python3' > .envrc && \
	direnv allow && \
	pip install --upgrade pip

.PHONY: pyreqs
pyreqs: requirements.txt 	## Load Python requirements
	pip install -r requirements.txt

.PHONY: changes
changes:	## create CHANGES file from git logs
	git log --oneline --pretty=format:"* %ad: %s" --date=short > CHANGES

