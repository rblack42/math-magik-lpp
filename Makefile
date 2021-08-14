# math-magik Makefile
PROJECT := math_magik
MK	:= mk

-include $(MK)/help.mk
-include $(MK)/sphinx.mk
-include $(MK)/python.mk

.PHONY: autodoc
autodoc: ## Generate code documentation
	cd mmdesigner && \
		python DataCatalog.py
