VENV		:=	.venv
PYTHON		:=	$(VENV)/bin/python
PYTHON_CAP	:=	$(VENV)/bin/python-cap
PIP		:=	$(VENV)/bin/pip
UV		:=	$(VENV)/bin/uv

NAME		=	jarbinlocalapi

PID_DIR		=	run
PID_FILE	=	$(PID_DIR)/$(NAME).pid
LOG_FILE	=	$(PID_DIR)/$(NAME).log

INSTALL_USER	:=	$(shell id -un)

SHELL		:=	/bin/bash
.DEFAULT_GOAL	=	help

.PHONY:	help install network run start stop restart status logs sync update clean test

help:
	@echo "Usage:"
	@echo "  make install  Install everything the API needs"
	@echo "  make network  Configure network access"
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

install:
	@python -c 'import sys; print(f"Detected Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"); \
	exit(0 if sys.version_info >= (3, 11) else 1)' || (echo "Error: Python 3.11 or newer is required." && exit 1)
	python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	sudo cp $$(readlink -f $(PYTHON)) $(PYTHON_CAP)
	sudo chown $$(id -u):$$(id -g) $(PYTHON_CAP)
	sudo setcap 'cap_net_bind_service=+ep' $(PYTHON_CAP)
	@$(MAKE) --no-print-directory network update

network:
	sudo hostnamectl set-hostname "$(INSTALL_USER)"
	sudo firewall-cmd --zone=FedoraWorkstation --add-port=80/tcp --permanent
	sudo firewall-cmd --reload
	sudo systemctl enable --now avahi-daemon
	@echo
	@echo "Network access configured."
	@echo
	@echo "JarbinLocalAPI:"
	@echo "  HTTP: http://$$(hostname)/"
	@echo "  mDNS: http://$$(hostname).local/"
	@echo

run:
	$(PYTHON_CAP) -m uvicorn jarbinlocalapi.main:jarbinlocalapi --host 0.0.0.0 --port 80

start:
	@mkdir -p $(PID_DIR)
	@if [ -f $(PID_FILE) ] && kill -0 $$(cat $(PID_FILE)) 2>/dev/null; then \
		echo "$(NAME) is already running (PID $$(cat $(PID_FILE)))"; \
	else \
		echo "Starting $(NAME)..."; \
		$(PYTHON_CAP) -m uvicorn jarbinlocalapi.main:jarbinlocalapi --host 0.0.0.0 --port 80 > $(LOG_FILE) 2>&1 & \
		echo $$! > $(PID_FILE); \
		sleep 1; \
		if kill -0 $$(cat $(PID_FILE)) 2>/dev/null; then \
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
		if kill -0 $$PID 2>/dev/null; then \
			echo "Stopping $(NAME) (PID $$PID)..."; \
			kill $$PID; \
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
	@if [ -f $(PID_FILE) ] && kill -0 $$(cat $(PID_FILE)) 2>/dev/null; then \
		echo "$(NAME) is running (PID $$(cat $(PID_FILE)))"; \
	else \
		echo "$(NAME) is not running"; \
	fi

logs:
	cat $(LOG_FILE) | tail -n 100

sync:
	$(UV) sync

update:
	$(UV) lock --upgrade
	@$(MAKE) --no-print-directory sync

clean:
	sudo find . -type d -name "__pycache__" -exec rm -rf {} +
	sudo find . -type f -name "*.pyc" -delete
	sudo rm -drf $(PID_DIR)

test:
	$(PYTHON) -m tests
