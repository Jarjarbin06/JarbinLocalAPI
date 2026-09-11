# JarbinLocalAPI — Ideas & Architecture

> A modular local API and web interface designed to provide reusable services for Jarbin's applications and development projects.

## Overview

The current architecture is:

```text
Device on local network
        │
        ▼
jarjarbin.local
        │
        ▼
     FastAPI
        │
        ├── System
        ├── GitHub
        ├── JarEngine
        ├── Configuration
        ├── Logging
        ├── Services
        ├── Files / Packages
        ├── Notifications
        ├── Clipboard
        ├── Jobs
        └── Documentation
```

The main goal is to make **JarbinLocalAPI a reusable local infrastructure layer** rather than a single-purpose API.

The current implementation focuses on the **system information and monitoring service** and its web interface.

---

# 1. GitHub API Aggregator

## Goal

Provide a local API around GitHub so that other applications do not need to communicate directly with GitHub.

This could centralize:

* repositories;
* issues;
* pull requests;
* commits;
* releases;
* repository statistics;
* GitHub activity;
* authenticated requests.

## Example API

```http
GET /github/repos
GET /github/repos/{owner}/{repo}
GET /github/repos/{owner}/{repo}/issues
GET /github/repos/{owner}/{repo}/pulls
GET /github/repos/{owner}/{repo}/commits
GET /github/repos/{owner}/{repo}/releases
GET /github/activity
```

Example:

```http
GET /github/repos/Jarjarbin06/Jarbin-ToolKit
```

```json
{
    "name": "Jarbin-ToolKit",
    "stars": 12,
    "forks": 2,
    "open_issues": 3
}
```

## Possible implementation

```text
FastAPI
   │
   ▼
GitHub service
   │
   ▼
GitHub REST API
```

The service could also cache frequently requested information to avoid unnecessary GitHub API calls.

**Status:** Planned.

---

# 2. JarEngine Data Service

## Goal

Provide **only persistent data storage and retrieval** for JarEngine.

This service should not handle multiplayer synchronization or game networking.

Possible uses:

* save games;
* player data;
* game configuration;
* statistics;
* progression;
* persistent world data.

## Example API

```http
GET  /jarengine/data/{game}/{key}
PUT  /jarengine/data/{game}/{key}
DELETE /jarengine/data/{game}/{key}
```

Example:

```http
PUT /jarengine/data/my_game/player_42
```

```json
{
    "level": 17,
    "experience": 8420,
    "inventory": [
        "sword",
        "potion"
    ]
}
```

Then:

```http
GET /jarengine/data/my_game/player_42
```

returns the stored data.

## Important separation

The data service should remain independent from the multiplayer middleware:

```text
JarEngine
   │
   ├── Persistent data ──► /jarengine/data
   │
   └── Multiplayer sync ─► /jarengine/middleware
```

**Status:** Planned.

---

# 3. JarEngine Multiplayer Middleware

## Goal

Provide a **fast local-network communication service** for synchronizing JarEngine multiplayer games.

This is deliberately separate from the data service.

The main purpose is:

> Fast temporary communication, not persistent storage.

Potential data:

* player positions;
* player actions;
* entity states;
* game events;
* lobby information;
* connection state.

## Possible architecture

```text
JarEngine A
     │
     │ fast messages
     ▼
JarbinLocalAPI
     │
     │ fast messages
     ▼
JarEngine B
```

The middleware should use persistent connections rather than traditional request/response HTTP where appropriate.

Possible technologies to investigate:

* FastAPI WebSockets;
* UDP-based communication for latency-sensitive data;
* an in-memory message broker implemented specifically for the project.

For the first implementation, **FastAPI WebSockets** would be the natural Python-only starting point.

## Example

```text
WS /jarengine/middleware/{game_id}
```

A client could send:

```json
{
    "type": "player_update",
    "player_id": 42,
    "position": [120.4, 83.1],
    "rotation": 90.0
}
```

The middleware broadcasts the update to the other connected players.

**Status:** Planned.

---

# 4. Central Configuration Service

## Goal

Store configuration centrally for Jarbin's applications.

Instead of having configuration duplicated across projects:

```text
JarEngine/config.json
JarTest/config.json
XITViewer/config.json
JCCS/config.json
```

applications could retrieve their configuration from JarbinLocalAPI.

## Example API

```http
GET /config/{application}
GET /config/{application}/{key}
PUT /config/{application}/{key}
```

Example:

```http
GET /config/jarengine
```

```json
{
    "debug": true,
    "log_level": "INFO",
    "autosave_interval": 0.5
}
```

This could also support application-specific configuration versions later.

**Status:** Planned.

---

# 5. Central Logging Service

## Goal

Allow every Jarbin application to send logs to one central service.

## Example API

```http
POST /logs
GET  /logs
GET  /logs/{application}
GET  /logs/{application}/errors
```

Example:

```json
{
    "application": "JarEngine",
    "level": "WARNING",
    "message": "Failed to load texture",
    "timestamp": "2026-09-02T19:32:00"
}
```

## Dashboard integration

The web dashboard could display:

```text
Recent logs

19:32:10  INFO     JarEngine started
19:32:14  INFO     Save completed
19:33:02  WARNING  Texture missing
19:33:08  ERROR    Network connection failed
```

## Important consideration

The logging service should be designed to avoid becoming a performance bottleneck.

Applications should ideally be able to:

* buffer logs;
* send them in batches;
* optionally disable remote logging;
* define minimum log levels.

**Status:** Planned.

---

# 6. Application Heartbeat / Service Registry

## Goal

Keep track of applications currently running on the network.

An application registers itself:

```http
POST /services/register
```

```json
{
    "name": "JarEngine",
    "version": "1.4.2",
    "address": "192.168.1.50",
    "port": 4242
}
```

It then periodically sends a heartbeat:

```http
POST /services/{service_id}/heartbeat
```

The server can expose:

```http
GET /services
GET /services/{name}
```

Example:

```json
[
    {
        "name": "JarEngine",
        "status": "online"
    },
    {
        "name": "JarTest",
        "status": "online"
    },
    {
        "name": "XITViewer",
        "status": "offline"
    }
]
```

The dashboard could then show:

```text
SERVICES

● JarEngine       ONLINE
● JarTest         ONLINE
○ XITViewer       OFFLINE
```

A timeout could automatically mark a service as offline.

**Status:** Planned.

---

# 7. Local System Information API

## Goal

Expose useful information about the host machine.

The current implementation provides system information and monitoring through:

```http
GET /api/system
GET /api/system/cpu
GET /api/system/memory
GET /api/system/disk
GET /api/system/network
GET /api/system/processes
GET /api/system/sensors
GET /api/system/system
```

Categories are used where appropriate:

```http
GET /api/system/sensors?category=temperatures
GET /api/system/sensors?category=fans
GET /api/system/sensors?category=battery
GET /api/system/processes?category=count
GET /api/system/processes?category=pids
GET /api/system/processes?category=processes
```

The service currently exposes information such as:

* CPU usage and statistics;
* memory usage;
* disk usage and I/O;
* network interfaces and connections;
* running processes;
* temperatures;
* fans;
* battery information;
* boot time;
* logged-in users.

The implementation uses Python system libraries such as `psutil`.

The web interface consumes this API to display the information through the local dashboard.

**Status:** Implemented.

---

# 8. Download / Build Server

> **Optional — may not be implemented.**

## Goal

Use JarbinLocalAPI as a lightweight local build/download server.

Possible operations:

```http
POST /build/{project}
GET  /build/{project}/status
GET  /build/{project}/artifacts
```

Example workflow:

```text
POST /build/jarengine
        │
        ▼
   Git repository
        │
        ▼
      Build
        │
        ▼
     Run tests
        │
        ▼
    Build artifact
```

This could eventually become a small personal CI-like system.

However, this is lower priority than the core API services.

**Status:** Optional.

---

# 9. Jarbin Notifications

## Goal

Create a generic notification service for applications.

Example:

```http
POST /notifications
```

```json
{
    "title": "Build finished",
    "message": "JarEngine compiled successfully",
    "level": "success"
}
```

Possible notification targets could eventually include:

* the web dashboard;
* a phone application;
* desktop notifications;
* other registered clients.

The service itself should remain generic.

**Status:** Planned.

---

# 10. Clipboard Synchronization

## Goal

Create a personal LAN clipboard similar to the **Windows Phone Link / phone-to-PC clipboard synchronization concept**.

The server temporarily stores the latest clipboard content.

## Example

PC:

```http
PUT /clipboard
```

```json
{
    "text": "Some copied text"
}
```

Phone:

```http
GET /clipboard
```

returns:

```json
{
    "text": "Some copied text"
}
```

It could eventually support:

* text;
* images;
* timestamps;
* source device;
* clipboard history.

A possible architecture:

```text
PC clipboard
      │
      ▼
JarbinLocalAPI
      │
      ▼
Phone clipboard
```

For automatic synchronization, clients could maintain a WebSocket connection and receive clipboard-change events.

**Status:** Planned.

---

# 11. Remote Command / Job Queue

## Goal

Allow devices to request predefined operations on the Fedora machine.

Rather than exposing arbitrary shell execution, the API should expose **controlled jobs**.

Example:

```http
POST /jobs/jarengine/build
POST /jobs/jarengine/test
POST /jobs/jartest/run
POST /jobs/project/update
```

The server maintains a queue:

```text
Phone
  │
  ▼
POST /jobs/jarengine/build
  │
  ▼
Job Queue
  │
  ▼
Worker
  │
  ├── git
  ├── make
  └── tests
```

Example job status:

```http
GET /jobs/{job_id}
```

```json
{
    "id": "a82f31",
    "status": "running",
    "progress": 64
}
```

## Security

This should **never** become:

```http
POST /execute
{
    "command": "rm -rf ..."
}
```

Jobs should be explicitly registered server-side.

For example:

```text
jarengine_build
jarengine_tests
jartest_run
project_update
```

Each job maps to a known Python function or controlled command.

**Status:** Planned.

---

# 12. Personal Package / Cache Server

> **Scope: compressed packages only.**

## Goal

Store and distribute compressed packages locally.

For example:

```text
/packages
    Jarbin-ToolKit-1.2.0.tar.gz
    JarTest-0.8.1.tar.gz
    JarEngine-2.0.0.zip
```

Possible API:

```http
GET  /packages
POST /packages
GET  /packages/{package}
DELETE /packages/{package}
```

Example:

```http
GET /packages/Jarbin-ToolKit-1.2.0.tar.gz
```

The server could provide:

* package metadata;
* versions;
* checksums;
* upload/download;
* optional automatic cleanup.

This is **not intended to become a full PyPI/npm package registry**.

**Status:** Planned.

---

# 13. Personal Documentation API

## Goal

Provide a centralized API for Jarbin's personal and project documentation.

This could connect the other services and provide a single documentation layer for the local infrastructure.

Possible structure:

```text
/docs
    /jarengine
    /jartest
    /jarbin-toolkit
    /jccs
    /xitviewer
```

Example:

```http
GET /docs
GET /docs/jarengine
GET /docs/jarengine/api
GET /docs/jartest
```

A document could contain:

```json
{
    "title": "JarEngine API",
    "version": "1.4",
    "content": "...",
    "updated_at": "2026-09-02T18:30:00"
}
```

The documentation API could later expose:

* Markdown documents;
* project indexes;
* API references;
* changelogs;
* examples;
* tutorials;
* search.

**Status:** Planned.

---

# 14. Web Dashboard

## Goal

Make:

```text
http://jarjarbin.local/
```

the main human-facing entry point to JarbinLocalAPI.

The dashboard provides a web interface over the local services while the REST/WebSocket API remains the machine-facing interface.

The current implementation already provides a system dashboard with dedicated views for:

```text
/system
/system/cpu
/system/memory
/system/battery
/system/disk
/system/network
/system/processes
/system/system
/system/temperatures
/system/top_processes
```

## Python-only requirement

The application-side implementation should remain Python-based.

FastAPI handles routing and service access, while Jinja2 is used for server-side HTML rendering.

Architecture:

```text
Browser
   │
   ▼
FastAPI
   │
   ├── System service
   ├── Service registry
   ├── Logging service
   ├── GitHub service
   ├── Documentation service
   └── Other services
   │
   ▼
Jinja2 templates
   │
   ▼
HTML
   │
   ▼
Browser
```

The dashboard does not require a frontend framework.

A JavaScript-free implementation can use:

* normal HTML links;
* server-side rendering;
* HTML forms;
* CSS;
* automatic page refreshes.

For example:

```html
<meta http-equiv="refresh" content="5">
```

JavaScript may be used where useful for live updates, but the core dashboard should not depend on a JavaScript framework.

### Dashboard concept

```text
┌─────────────────────────────────────────────────┐
│                 JARBIN LOCAL                    │
├─────────────────────────────────────────────────┤
│                                                 │
│ SYSTEM                                          │
│ CPU       23%       RAM       8.2 / 15.5 GB     │
│ Disk      421 GB    Uptime    14h 23m           │
│                                                 │
├─────────────────────────────────────────────────┤
│ SERVICES                                        │
│                                                 │
│ ● JarEngine          ONLINE                     │
│ ● JarTest            ONLINE                     │
│ ○ XITViewer          OFFLINE                    │
│                                                 │
├─────────────────────────────────────────────────┤
│ RECENT LOGS                                     │
│                                                 │
│ INFO     JarEngine started                      │
│ INFO     Save completed                         │
│ WARNING  Texture missing                        │
│                                                 │
├─────────────────────────────────────────────────┤
│ QUICK ACCESS                                    │
│                                                 │
│ GitHub     Documentation     Packages           │
│ Clipboard  Jobs             Notifications       │
│                                                 │
└─────────────────────────────────────────────────┘
```

The dashboard should therefore remain the **human-facing interface**, while the API remains the **machine-facing interface**.

**Status:** Partially implemented.

---

The key principle should be:

> **JarbinLocalAPI provides reusable local infrastructure; individual applications consume that infrastructure without needing to implement the same functionality themselves.**
