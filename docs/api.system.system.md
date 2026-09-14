# `GET /api/system/system`

> `Return general system information or a selected system information category.`

---

## 🔹 Description

**Returns general system information including boot time and logged-in users.**

The optional `category` query parameter limits the response to either boot time or user information.

---

## 🔹 Request

### Method

`GET`

### Path

`/api/system/system`

### Authentication

`None`

### Path Parameters

| Parameter | Type | Required | Description                     |
| --------- | ---- | -------: | ------------------------------- |
| None      | —    |        — | No path parameters are defined. |

### Query Parameters

| Parameter  | Type     | Required | Default | Allowed Values       | Description                                     |
| ---------- | -------- | -------: | ------- | -------------------- | ----------------------------------------------- |
| `category` | `string` |       No | `None`  | `boot_time`, `users` | Selects a specific system information category. |

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
get_system_overview()
    │
    ▼
Select category if provided
    │
    ▼
JSON Response
```

1. Receive the request.
2. Validate the optional `category` parameter.
3. Collect general system information using `get_system_overview()`.
4. Return the complete response or selected category.

---

## 🔹 Response

### Success

**Status:** `200 OK`

**Content-Type:** `application/json`

```json
{
    "boot_time": 0.0,
    "users": []
}
```

### Response Fields

| Field       | Type     | Description                                  |
| ----------- | -------- | -------------------------------------------- |
| `boot_time` | `number` | System boot time represented as a timestamp. |
| `users`     | `array`  | Currently logged-in system users.            |

---

## 🔹 Metadata

No route-specific metadata is returned by the route itself.

API response metadata may be added by the global API middleware.

---

## 🔹 Status Codes

| Status | Meaning                                             |
| -----: | --------------------------------------------------- |
|  `200` | System information was returned successfully.       |
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
GET /api/system/system
```

### Response

```json
{
    "boot_time": 1750000000.0,
    "users": []
}
```

### Request with Parameters

```http
GET /api/system/system?category=boot_time
```

### Response

```json
{
    "boot_time": 1750000000.0
}
```

---

## 🔹 Data Contract

```text
System
├── boot_time: number
└── users: array
```

---

## 🔹 Dependencies

* `FastAPI`
* `Query`
* `Literal`
* `get_system_overview()`
* General system information services

---

## 🔹 Side Effects

* Reads system boot time.
* Reads logged-in user information.
* No persistent system state is modified.

---

## 🔹 Performance

The route performs lightweight system information queries. User enumeration may depend on the number of active sessions.

---

## 🔹 Security

* No authentication is required.
* The endpoint exposes system uptime information and logged-in user information.

---

## 🔹 Implementation

* **Module:** `jarbinlocalapi.api`
* **Route Function:** `get_api_system_system`
* **Service:** `get_system_overview()`
* **Router:** `api`

---

## 🔹 Route Contract

```text
METHOD      GET
PATH        /api/system/system
AUTH        None
PARAMETERS  category
BODY        None
RESPONSE    JSON
SUCCESS     200
ERRORS      422
```

---

## 🔹 Notes

* `boot_time` is returned as a timestamp.
* `users` contains information about currently logged-in users.
* `category` accepts `boot_time` or `users`.
