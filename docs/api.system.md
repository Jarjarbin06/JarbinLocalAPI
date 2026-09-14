# `GET /api/system`

> `Return complete system information or a selected system information category.`

---

## 🔹 Description

**Returns a complete overview of the system or a specific system information category.**

Without a query parameter, the route returns CPU, memory, disk, network, process, sensor, and system information.

The optional `type` query parameter limits the response to one category.

---

## 🔹 Request

### Method

`GET`

### Path

`/api/system`

### Authentication

`None`

### Path Parameters

| Parameter | Type | Required | Description                     |
| --------- | ---- | -------: | ------------------------------- |
| None      | —    |        — | No path parameters are defined. |

### Query Parameters

| Parameter | Type     | Required | Default | Allowed Values                                                       | Description                                     |
| --------- | -------- | -------: | ------- | -------------------------------------------------------------------- | ----------------------------------------------- |
| `type`    | `string` |       No | `None`  | `cpu`, `memory`, `disk`, `network`, `processes`, `sensors`, `system` | Selects a specific system information category. |

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
Validate "type" query parameter
    │
    ▼
Collect system information
    │
    ▼
Filter category if "type" is provided
    │
    ▼
JSON Response
```

1. Receive the `GET /api/system` request.
2. Validate the optional `type` parameter.
3. Collect the complete system overview using `get_overview()`.
4. Return the complete overview or the selected category.

---

## 🔹 Response

### Success

**Status:** `200 OK`

**Content-Type:** `application/json`

Without `type`, the response contains all available system categories:

```json
{
    "cpu": {},
    "memory": {},
    "disk": {},
    "network": {},
    "processes": {},
    "sensors": {},
    "system": {}
}
```

With `type=cpu`, for example:

```json
{
    "cpu": {}
}
```

### Response Fields

| Field       | Type     | Description                                       |
| ----------- | -------- | ------------------------------------------------- |
| `cpu`       | `object` | CPU information.                                  |
| `memory`    | `object` | Memory and swap information.                      |
| `disk`      | `object` | Disk usage, partitions, and I/O information.      |
| `network`   | `object` | Network interfaces, status, I/O, and connections. |
| `processes` | `object` | Process count, PIDs, and process information.     |
| `sensors`   | `object` | Temperature, fan, and battery information.        |
| `system`    | `object` | System boot time and logged-in user information.  |

When `type` is specified, only the selected field is returned.

---

## 🔹 Metadata

No route-specific metadata is returned by the route itself.

API response metadata may be added by the global API middleware.

---

## 🔹 Status Codes

| Status | Meaning                                               |
| -----: | ----------------------------------------------------- |
|  `200` | System information was collected successfully.        |
|  `422` | The `type` query parameter contains an invalid value. |

---

## 🔹 Errors

### `422 Unprocessable Entity`

```json
{
    "detail": [
        {
            "loc": [
                "query",
                "type"
            ],
            "msg": "<validation error>",
            "type": "<error type>"
        }
    ]
}
```

**Cause:** The `type` parameter is not one of the values defined by the route's `Literal` type.

---

## 🔹 Examples

### Request

```http
GET /api/system
```

### Response

```json
{
    "cpu": {},
    "memory": {},
    "disk": {},
    "network": {},
    "processes": {},
    "sensors": {},
    "system": {}
}
```

### Request with Parameters

```http
GET /api/system?type=cpu
```

### Response

```json
{
    "cpu": {}
}
```

---

## 🔹 Data Contract

```text
SystemOverview
├── cpu: object
├── memory: object
├── disk: object
├── network: object
├── processes: object
├── sensors: object
└── system: object
```

When `type` is specified:

```text
SystemCategory
└── <type>: object
```

---

## 🔹 Dependencies

* `FastAPI`
* `Query`
* `Literal`
* `get_overview()`
* System information services

---

## 🔹 Side Effects

* Reads system information.
* Reads process and network state.
* No persistent system state is modified.

---

## 🔹 Performance

The route collects multiple system information categories for each request when no `type` filter is specified.

Using `type` still collects the complete overview before selecting the requested category.

---

## 🔹 Security

* No authentication is required.
* The endpoint exposes local system information.
* Access should be restricted to trusted local network clients.

---

## 🔹 Implementation

* **Module:** `jarbinlocalapi.api`
* **Route Function:** `get_api_system`
* **Service:** `get_overview()`
* **Router:** `api`

---

## 🔹 Route Contract

```text
METHOD      GET
PATH        /api/system
AUTH        None
PARAMETERS  type
BODY        None
RESPONSE    JSON
SUCCESS     200
ERRORS      422
```

---

## 🔹 Notes

* Without `type`, all system information categories are returned.
* `type` is validated by FastAPI using a `Literal` type.
* The route does not define separate endpoints for individual categories.
