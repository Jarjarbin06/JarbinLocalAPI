# `GET /api/system/memory`

> `Return memory system information or a selected memory category.`

---

## 🔹 Description

**Returns virtual memory and swap information collected by the memory service.**

The optional `category` query parameter limits the response to either virtual memory or swap information.

---

## 🔹 Request

### Method

`GET`

### Path

`/api/system/memory`

### Authentication

`None`

### Path Parameters

| Parameter | Type | Required | Description                     |
| --------- | ---- | -------: | ------------------------------- |
| None      | —    |        — | No path parameters are defined. |

### Query Parameters

| Parameter  | Type     | Required | Default | Allowed Values    | Description                         |
| ---------- | -------- | -------: | ------- | ----------------- | ----------------------------------- |
| `category` | `string` |       No | `None`  | `virtual`, `swap` | Selects a specific memory category. |

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
get_memory_overview()
    │
    ▼
Select category if provided
    │
    ▼
JSON Response
```

1. Receive the request.
2. Validate the optional `category` parameter.
3. Collect memory information using `get_memory_overview()`.
4. Return the complete response or selected category.

---

## 🔹 Response

### Success

**Status:** `200 OK`

**Content-Type:** `application/json`

```json
{
    "virtual": {},
    "swap": {}
}
```

### Response Fields

| Field     | Type     | Description                 |
| --------- | -------- | --------------------------- |
| `virtual` | `object` | Virtual memory information. |
| `swap`    | `object` | Swap memory information.    |

---

## 🔹 Metadata

No route-specific metadata is returned by the route itself.

API response metadata may be added by the global API middleware.

---

## 🔹 Status Codes

| Status | Meaning                                             |
| -----: | --------------------------------------------------- |
|  `200` | Memory information was returned successfully.       |
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
GET /api/system/memory
```

### Response

```json
{
    "virtual": {},
    "swap": {}
}
```

### Request with Parameters

```http
GET /api/system/memory?category=virtual
```

### Response

```json
{
    "virtual": {}
}
```

---

## 🔹 Data Contract

```text
Memory
├── virtual: object
└── swap: object
```

---

## 🔹 Dependencies

* `FastAPI`
* `Query`
* `Literal`
* `get_memory_overview()`
* Memory system information services

---

## 🔹 Side Effects

* Reads virtual memory information.
* Reads swap information.
* No persistent system state is modified.

---

## 🔹 Performance

Memory information is collected on each request.

---

## 🔹 Security

* No authentication is required.
* The endpoint exposes local memory information.

---

## 🔹 Implementation

* **Module:** `jarbinlocalapi.api`
* **Route Function:** `get_api_system_memory`
* **Service:** `get_memory_overview()`
* **Router:** `api`

---

## 🔹 Route Contract

```text
METHOD      GET
PATH        /api/system/memory
AUTH        None
PARAMETERS  category
BODY        None
RESPONSE    JSON
SUCCESS     200
ERRORS      422
```

---

## 🔹 Notes

* `category` accepts `virtual` or `swap`.
* Without `category`, both categories are returned.

---
