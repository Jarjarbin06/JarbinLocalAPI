# `GET /api/system/processes`

> `Return process system information or a selected process category.`

---

## 🔹 Description

**Returns process count, process identifiers, and process information collected from the system.**

The optional `category` query parameter limits the response to one process information category.

---

## 🔹 Request

### Method

`GET`

### Path

`/api/system/processes`

### Authentication

`None`

### Path Parameters

| Parameter | Type | Required | Description                     |
| --------- | ---- | -------: | ------------------------------- |
| None      | —    |        — | No path parameters are defined. |

### Query Parameters

| Parameter  | Type     | Required | Default | Allowed Values               | Description                                      |
| ---------- | -------- | -------: | ------- | ---------------------------- | ------------------------------------------------ |
| `category` | `string` |       No | `None`  | `count`, `pids`, `processes` | Selects a specific process information category. |

### Headers

| Header | Required | Description                       |
| ------ | -------: | --------------------------------- |
| None   |        — | No specific headers are required. |

### Body

No request body is required.

---

## 🔹 Settings

| Setting        | Value  |
| -------------- | ------ |
| Response Type  | `JSON` |
| Authentication | `None` |
| Cacheable      | `No`   |
| Streaming      | `No`   |
| Idempotent     | `Yes`  |

---

## 🔹 Processing

```text
Request
    │
    ▼
Validate "category"
    │
    ▼
get_processes_overview()
    │
    ▼
Select category if provided
    │
    ▼
JSON Response
```

1. Receive the request.
2. Validate the optional `category` parameter.
3. Collect process information using `get_processes_overview()`.
4. Return the complete response or selected category.

---

## 🔹 Response

### Success

**Status:** `200 OK`

**Content-Type:** `application/json`

```json
{
    "count": 0,
    "pids": [],
    "processes": []
}
```

### Response Fields

| Field       | Type      | Description                   |
| ----------- | --------- | ----------------------------- |
| `count`     | `integer` | Number of detected processes. |
| `pids`      | `array`   | Process identifiers.          |
| `processes` | `array`   | Process information.          |

Each process entry may contain:

```text
Process
├── pid: integer
├── name: string
├── status: string
├── cpu_percent: number
├── memory_info: object
└── memory_percent: number
```

---

## 🔹 Metadata

No route-specific metadata is returned by the route itself.

API response metadata may be added by the global API middleware.

---

## 🔹 Status Codes

| Status | Meaning                                             |
| -----: | --------------------------------------------------- |
|  `200` | Process information was returned successfully.      |
|  `422` | The `category` parameter contains an invalid value. |

---

## 🔹 Errors

### `422 Unprocessable Entity`

```json
{
    "detail": [
        {
            "loc": ["query", "category"],
            "msg": "<validation error>",
            "type": "<error type>"
        }
    ]
}
```

**Cause:** The requested category is not defined by the route.

---

## 🔹 Examples

### Request

```http
GET /api/system/processes
```

### Response

```json
{
    "count": 120,
    "pids": [1, 2, 3],
    "processes": []
}
```

### Request with Parameters

```http
GET /api/system/processes?category=count
```

### Response

```json
{
    "count": 120
}
```

---

## 🔹 Data Contract

```text
Processes
├── count: integer
├── pids: array
└── processes: array
    └── Process
        ├── pid: integer
        ├── name: string
        ├── status: string
        ├── cpu_percent: number
        ├── memory_info: object
        └── memory_percent: number
```

---

## 🔹 Dependencies

* `FastAPI`
* `Query`
* `Literal`
* `get_processes_overview()`
* Process system information services

---

## 🔹 Side Effects

* Reads process information.
* Reads process identifiers.
* No process state is modified.

---

## 🔹 Performance

Process enumeration may require inspecting multiple running processes and can therefore be more expensive than static system information queries.

---

## 🔹 Security

* No authentication is required.
* The endpoint exposes local process information.
* Process information may reveal application names and resource usage.

---

## 🔹 Implementation

* **Module:** `jarbinlocalapi.api`
* **Route Function:** `get_api_system_processes`
* **Service:** `get_processes_overview()`
* **Router:** `api`

---

## 🔹 Route Contract

```text
METHOD      GET
PATH        /api/system/processes
AUTH        None
PARAMETERS  category
BODY        None
RESPONSE    JSON
SUCCESS     200
ERRORS      422
```

---

## 🔹 Notes

* `processes` contains detailed process entries.
* `pids` contains only process identifiers.
* `count` contains the total process count.

---
