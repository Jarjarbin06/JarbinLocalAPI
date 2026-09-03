NAME	=	jarbinlocalapi
UV	=	uv

.DEFAULT_GOAL	=	run

.PHONY:	help run sync update clean clean-run

help:
	@echo "Usage:"
	@echo "  make run      Run the FastAPI server"
	@echo "  make sync     Synchronize the virtual environment"
	@echo "  make update   Update dependencies"
	@echo "  make clean    Remove generated Python files"

run:
	sudo $(UV) run uvicorn jarbinlocalapi.main:jarbinlocalapi --host 0.0.0.0 --port 80

sync:
	$(UV) sync

update:
	$(UV) lock --upgrade
	@$(MAKE) --no-print-directory sync

clean:
	sudo find . -path './.venv' -o -type d -name "__pycache__" -exec rm -rf {} +
	sudo find . -path './.venv' -o -type f -name "*.pyc" -delete
