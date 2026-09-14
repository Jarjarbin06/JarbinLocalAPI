# 📦 JarbinLocalAPI — Route Reference

> Complete HTTP route index for the JarbinLocalAPI server.

---

## 🔹 Route Overview

JarbinLocalAPI exposes three main route groups:

```text
JarbinLocalAPI
│
├── Root
│   └── /
│
├── Updater
│   └── /
│
├── API
│   ├── /api/
│   ├── /api/system
│   └── /api/system/*
│
└── Application
    ├── /app
    └── /app/system/*
```

API routes expose structured machine-readable data.

Application routes expose the web interface and documentation-oriented views.

---

## 🔹 Root Routes

| Method | Path | Description       | Documentation        |
| -----: | ---- | ----------------- | -------------------- |
|  `GET` | `/`  | Get server status | [`root.md`](/doc/root) |

---

## 🔹 API Routes

### API Root

| Method | Path    | Description    | Documentation      |
| -----: | ------- | -------------- | ------------------ |
|  `GET` | `/api/` | Get API status | [`api.md`](/doc/api) |

### System

| Method | Path                    | Description                     | Documentation                                        |
| -----: | ----------------------- | ------------------------------- | ---------------------------------------------------- |
|  `GET` | `/api/system`           | Get complete system overview    | [`api.system.md`](/doc/api/system)                     |
|  `GET` | `/api/system/cpu`       | Get CPU information             | [`api.system.cpu.md`](/doc/api/system/cpu)             |
|  `GET` | `/api/system/memory`    | Get memory information          | [`api.system.memory.md`](/doc/api/system/memory)       |
|  `GET` | `/api/system/disk`      | Get disk information            | [`api.system.disk.md`](/doc/api/system/disk)           |
|  `GET` | `/api/system/network`   | Get network information         | [`api.system.network.md`](/doc/api/system/network)     |
|  `GET` | `/api/system/processes` | Get process information         | [`api.system.processes.md`](/doc/api/system/processes) |
|  `GET` | `/api/system/sensors`   | Get hardware sensor information | [`api.system.sensors.md`](/doc/api/system/sensors)     |
|  `GET` | `/api/system/system`    | Get system information          | [`api.system.system.md`](/doc/api/system/system)       |

### API System Route Structure

```text
/api/
│
└── system/
    │
    ├── cpu
    ├── memory
    ├── disk
    ├── network
    ├── processes
    ├── sensors
    └── system
```

The `/api/system` overview combines the results of the individual system services.

---

## 🔹 Application Routes

### Application Root

| Method | Path   | Description               | Documentation      |
| -----: | ------ | ------------------------- | ------------------ |
|  `GET` | `/app` | Main web application page | [`app.md`](/doc/app) |

### System

| Method | Path                        | Description                 | Documentation                                                |
| -----: | --------------------------- | --------------------------- | ------------------------------------------------------------ |
|  `GET` | `/app/system`               | System monitoring overview  | [`app.system.md`](/doc/app/system)                             |
|  `GET` | `/app/system/cpu`           | CPU monitoring page         | [`app.system.cpu.md`](/doc/app/system/cpu)                     |
|  `GET` | `/app/system/memory`        | Memory monitoring page      | [`app.system.memory.md`](/doc/app/system/memory)               |
|  `GET` | `/app/system/disk`          | Disk monitoring page        | [`app.system.disk.md`](/doc/app/system/disk)                   |
|  `GET` | `/app/system/network`       | Network monitoring page     | [`app.system.network.md`](/doc/app/system/network)             |
|  `GET` | `/app/system/processes`     | Process monitoring page     | [`app.system.processes.md`](/doc/app/system/processes)         |
|  `GET` | `/app/system/system`        | System information page     | [`app.system.system.md`](/doc/app/system/system)               |
|  `GET` | `/app/system/battery`       | Battery monitoring page     | [`app.system.battery.md`](/doc/app/system/battery)             |
|  `GET` | `/app/system/temperatures`  | Temperature monitoring page | [`app.system.temperatures.md`](/doc/app/system/temperatures)   |
|  `GET` | `/app/system/top_processes` | Top CPU-consuming processes | [`app.system.top_processes.md`](/doc/app/system/top_processes) |

### Application System Route Structure

```text
/app/
│
└── system/
    │
    ├── cpu
    ├── memory
    ├── disk
    ├── network
    ├── processes
    ├── system
    ├── battery
    ├── temperatures
    └── top_processes
```

---

## 🔹 Documentation Routes

The documentation interface provides access to the Markdown documentation files through the `/d` route.

```text
/d
│
│
├── /routes (this page)
│
│
├── /root
│
│
├── /api
│
├── /api/system
├── /api/system/cpu
├── /api/system/memory
├── /api/system/disk
├── /api/system/network
├── /api/system/processes
├── /api/system/sensors
├── /api/system/system
│
│
├── /app
│
├── /app/system
├── /app/system/cpu
├── /app/system/memory
├── /app/system/disk
├── /app/system/network
├── /app/system/processes
├── /app/system/system
├── /app/system/battery
├── /app/system/temperatures
└── /app/system/top_processes
```

Documentation URLs use the same route structure as the documented resource.

For example:

```text
/doc/api/system/cpu
```

loads:

```text
docs/api.system.cpu.md
```

---

## 🔹 Static Routes

| Method | Path        | Description                  |
|-------:|-------------|------------------------------|
|  `GET` | `/static/*` | Application static resources |

Static resources include:

```text
/static/
├── css/
├── html/
├── images/
└── js/
```

---

## 🔹 Special Routes

FastAPI also exposes automatically generated API documentation:

| Method | Path            | Description    |
| -----: | --------------- | -------------- |
|  `GET` | `/docs`         | Swagger UI     |
|  `GET` | `/redoc`        | ReDoc          |
|  `GET` | `/openapi.json` | OpenAPI schema |

These routes are generated by FastAPI and are not represented by individual Markdown files in `docs/`.

---

## 🔹 Complete Route Tree

```text
/
│
├── api/
│   │
│   └── system
│       ├── cpu
│       ├── memory
│       ├── disk
│       ├── network
│       ├── processes
│       ├── sensors
│       └── system
│
├── app
│   │
│   └── system
│       ├── cpu
│       ├── memory
│       ├── disk
│       ├── network
│       ├── processes
│       ├── system
│       ├── battery
│       ├── temperatures
│       └── top_processes
│
├── d
│   └── <documentation page>
│
├── static/*
│
├── docs
├── redoc
└── openapi.json
```

---

## 🔹 Route Categories

| Category      | Prefix            | Response Type | Purpose                         |
|---------------|-------------------|---------------|---------------------------------|
| Root          | `/`               | JSON          | Server status                   |+
| API           | `/api`            | JSON          | Machine-readable services       |
| Application   | `/app`            | HTML          | Web interface                   |
| Documentation | `/d`              | HTML          | Rendered Markdown documentation |
| Static        | `/static`         | Static        | Assets                          |
| FastAPI       | `/docs`, `/redoc` | HTML          | Generated API documentation     |
| OpenAPI       | `/openapi.json`   | JSON          | OpenAPI schema                  |

---

## 🔹 Notes

* This document is an index and does not replace individual route documentation.
* Route-specific behavior is documented in the corresponding Markdown file.
* The `/d` documentation paths mirror the documented route paths.
* API routes are intended for structured programmatic access.
* Application routes are intended for browser-based interaction.
* FastAPI-generated routes are managed by the framework.
