# `GET /api/system/cpu`

> `Return CPU system information or a selected CPU information category.`

---

## 🔹 Description

**Returns CPU information collected by the system CPU service.**

Without a query parameter, the route returns all available CPU information. The optional `category` query parameter limits the response to one CPU information category.

---

## 🔹 Request

### Method

`GET`

### Path

`/api/system/cpu`

### Authentication

`None`

### Path Parameters

| Parameter | Type | Required | Description                     |
| --------- | ---- | -------: | ------------------------------- |
| None      | —    |        — | No path parameters are defined. |

### Query Parameters

| Parameter  | Type     | Required | Default | Allowed Values                                                             | Description                                  |
| ---------- | -------- | -------: | ------- | -------------------------------------------------------------------------- | -------------------------------------------- |
| `category` | `string` |       No | `None`  | `percent`, `times`, `times_percent`, `count`, `stats`, `frequency`, `load` | Selects a specific CPU information category. |

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
get_cpu_overview()
    │
    ▼
Select category if provided
    │
    ▼
JSON Response
```

1. Receive the request.
2. Validate the optional `category` parameter.
3. Collect CPU information using `get_cpu_overview()`.
4. Return the complete response or the selected category.

---

## 🔹 Response

### Success

**Status:** `200 OK`

**Content-Type:** `application/json`

```json
{
    "percent": 0.0,
    "times": {},
    "times_percent": {},
    "count": 0,
    "stats": {},
    "frequency": {},
    "load": []
}
```

### Response Fields

| Field           | Type      | Description                                      |
| --------------- | --------- | ------------------------------------------------ |
| `percent`       | `number`  | Current CPU utilization percentage.              |
| `times`         | `object`  | CPU time information.                            |
| `times_percent` | `object`  | CPU time information represented as percentages. |
| `count`         | `integer` | Number of available CPUs.                        |
| `stats`         | `object`  | CPU statistics.                                  |
| `frequency`     | `object`  | CPU frequency information.                       |
| `load`          | `array`   | CPU load information.                            |

---

## 🔹 Metadata

No route-specific metadata is returned by the route itself.

API response metadata may be added by the global API middleware.

---

## 🔹 Status Codes

| Status | Meaning                                             |
| -----: | --------------------------------------------------- |
|  `200` | CPU information was returned successfully.          |
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
GET /api/system/cpu
```

### Response

```json
{
    "percent": 12.5,
    "times": {},
    "times_percent": {},
    "count": 8,
    "stats": {},
    "frequency": {},
    "load": []
}
```

### Request with Parameters

```http
GET /api/system/cpu?category=percent
```

### Response

```json
{
    "percent": 12.5
}
```

---

## 🔹 Data Contract

```text
CPU
├── percent: number
├── times: object
├── times_percent: object
├── count: integer
├── stats: object
├── frequency: object
└── load: array
```

---

## 🔹 Dependencies

* `FastAPI`
* `Query`
* `Literal`
* `get_cpu_overview()`
* CPU system information services

---

## 🔹 Side Effects

* Reads CPU information.
* No persistent system state is modified.

---

## 🔹 Performance

CPU information is collected on each request. No persistent result is maintained by the route.

---

## 🔹 Security

* No authentication is required.
* The endpoint exposes local CPU information.

---

## 🔹 Implementation

* **Module:** `jarbinlocalapi.api`
* **Route Function:** `get_api_system_cpu`
* **Service:** `get_cpu_overview()`
* **Router:** `api`

---

## 🔹 Route Contract

```text
METHOD      GET
PATH        /api/system/cpu
AUTH        None
PARAMETERS  category
BODY        None
RESPONSE    JSON
SUCCESS     200
ERRORS      422
```

---

## 🔹 Notes

* `category` is optional.
* The category is validated using a `Literal` type.
* Without `category`, all CPU categories are returned.

---
