# 📦 JarbinLocalAPI

> A modular local API and web interface designed to provide services to software running on a local network.

## 🔹 Short Description

**JarbinLocalAPI is a Python-based local API framework built with FastAPI, designed to centralize and expose local services through a structured HTTP interface.**

The first implemented service provides system information and monitoring.

## 🔹 Authors

* Nathan AMARAGGI (Jarjarbin)
* Jarbin06

## 🔹 License

GPL v3

## 🔹 Target Audience

* Developers building local software services
* Developers requiring a local HTTP interface
* Developers extending JarbinLocalAPI with additional services
* Linux users running local infrastructure

## 🔹 Platform Support

* **OS:** Fedora Linux
* **Python:** 3.11+
* **Framework:** FastAPI
* **Package management:** `uv` / `pip`

The current installation and network configuration are designed for Fedora Workstation.

## 🔹 Purpose

JarbinLocalAPI aims to provide a **centralized local API for multiple independent services**.

The project is designed to eventually provide services such as:

* System information
* File sharing
* JarEngine integration
* Configuration management
* Additional local utilities and services

It is **not a cloud API or remote service**, but a **local infrastructure API intended to run on a user's own system or network**.

## 🔹 Key Features

* FastAPI-based HTTP server
* Modular service architecture
* Server-rendered web interface
* Local network access
* mDNS support
* Fedora firewall integration
* Background server management
* `uv` dependency management
* JarTest integration testing

## 🔹 Architecture

```text
┌──────────────────────────────┐
│          Local Host          │
│                              │
│      ┌────────────────┐      │
│      │ JarbinLocalAPI │      │
│      └───────┬────────┘      │
│              │               │
│       ┌──────┴──────┐        │
│       ▼             ▼        │
│   API Services    Web App    │
│       │             │        │
│       └──────┬──────┘        │
│              │               │
│              ▼               │
│        Local Resources       │
└──────────────────────────────┘
```

Services are intended to remain modular so new functionality can be added without changing the fundamental API structure.

## 🔹 API Documentation

The complete API reference is maintained separately.

**[→ Open the API Documentation](docs/api.md)**

## 🔹 Project Structure

```text
jarbinlocalapi/
├── jarbinlocalapi/
│   ├── api/
│   │   └── ...
│   ├── app/
│   │   └── ...
│   └── main.py
│
├── tests/
├── docs/
├── Makefile
├── requirements.txt
└── pyproject.toml
```

## 🔹 Installation

Python 3.11 or newer is required.

```bash
make install
```

The installation configures the Python environment, dependencies, local hostname, firewall, and mDNS access.

> `sudo` required in order to setup network

## 🔹 Execution

Run in the foreground:

```bash
make run
```

Run in the background:

```bash
make start
```

Other server controls:

```bash
make stop
make restart
make status
make logs
```

The server listens on:

```text
0.0.0.0:80
```

It can be accessed locally through:

```text
http://<hostname>/
http://<hostname>.local/
```

## 🔹 Dependency Management

Synchronize the environment:

```bash
make sync
```

Update dependencies:

```bash
make update
```

## 🔹 Testing

JarbinLocalAPI uses JarTest for integration testing.

```bash
make test
```

## 🔹 Design Philosophy

* Modular services
* Local-first execution
* Structured interfaces
* Explicit system boundaries
* Reusable API components
* Minimal external dependencies
* Deterministic behavior

## 🔹 Current State

⚠️ **JarbinLocalAPI is actively developed. The current implementation focuses on system information and monitoring.**

Implemented:

* FastAPI server
* System information service
* System monitoring web interface
* Local network access
* mDNS configuration
* Server lifecycle management
* JarTest integration tests

Planned services include file sharing, JarEngine middleware, configuration centralization, and additional local services.

> See [→ Routes](TODO_Routes.md) and [→ Updater](TODO_Updater.md) for planned features (plan made with IA)

## 🔹 Limitations

* Current installation and network configuration target Fedora Linux.
* Port 80 requires the configured privileged Python launcher.
* Some system information depends on host hardware and operating-system capabilities.
* The project is currently intended for local-network use.

## 🔹 Notes

JarbinLocalAPI is intended to become a **central local service layer** for Jarjarbin06 software and other compatible applications.

The current system service is the first implementation of this architecture; additional services can be integrated independently as the project develops.
