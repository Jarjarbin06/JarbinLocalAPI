NAME	=	jarbinlocalapi
UV	=	uv

PID_DIR	=	run
PID_FILE	=	$(PID_DIR)/$(NAME).pid
LOG_FILE	=	$(PID_DIR)/$(NAME).log

.DEFAULT_GOAL	=	run

.PHONY:	help run start stop restart status logs sync update clean test

help:
	@echo "Usage:"
	@echo "  make run      Run the FastAPI server in foreground"
	@echo "  make start    Start the FastAPI server in background"
	@echo "  make stop     Stop the FastAPI server"
	@echo "  make restart  Restart the FastAPI server"
	@echo "  make status   Show server status"
	@echo "  make logs     Show server logs"
	@echo "  make sync     Synchronize the virtual environment"
	@echo "  make update   Update dependencies"
	@echo "  make clean    Remove generated Python files"
	@echo "  make test     Run JarTest"

run:
	sudo .venv/bin/uvicorn jarbinlocalapi.main:jarbinlocalapi --host 0.0.0.0 --port 80

start:
	@mkdir -p $(PID_DIR)
	@if [ -f $(PID_FILE) ] && sudo kill -0 $$(cat $(PID_FILE)) 2>/dev/null; then \
		echo "$(NAME) is already running (PID $$(cat $(PID_FILE)))"; \
	else \
		echo "Starting $(NAME)..."; \
		sudo sh -c '.venv/bin/uvicorn jarbinlocalapi.main:jarbinlocalapi --host 0.0.0.0 --port 80 > $(LOG_FILE) 2>&1 & echo $$! > $(PID_FILE)'; \
		sleep 1; \
		if sudo kill -0 $$(cat $(PID_FILE)) 2>/dev/null; then \
			echo "$(NAME) started (PID $$(cat $(PID_FILE)))"; \
		else \
			echo "Failed to start $(NAME)"; \
			rm -f $(PID_FILE); \
			exit 1; \
		fi \
	fi

stop:
	@if [ ! -f $(PID_FILE) ]; then \
		echo "$(NAME) is not running"; \
	else \
		PID=$$(cat $(PID_FILE)); \
		if sudo kill -0 $$PID 2>/dev/null; then \
			echo "Stopping $(NAME) (PID $$PID)..."; \
			sudo kill $$PID; \
			rm -f $(PID_FILE); \
			echo "$(NAME) stopped"; \
		else \
			echo "$(NAME) process not found"; \
			rm -f $(PID_FILE); \
		fi \
	fi

restart:
	@$(MAKE) --no-print-directory stop
	@$(MAKE) --no-print-directory start

status:
	@if [ -f $(PID_FILE) ] && sudo kill -0 $$(cat $(PID_FILE)) 2>/dev/null; then \
		echo "$(NAME) is running (PID $$(cat $(PID_FILE)))"; \
	else \
		echo "$(NAME) is not running"; \
	fi

logs:
	tail -f $(LOG_FILE)

sync:
	$(UV) sync

update:
	$(UV) lock --upgrade
	@$(MAKE) --no-print-directory sync

clean:
	sudo find . -path './.venv' -o -type d -name "__pycache__" -exec rm -rf {} +
	sudo find . -path './.venv' -o -type f -name "*.pyc" -delete
	rm -drf run

test:
	.venv/bin/python3 -m tests