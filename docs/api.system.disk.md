# `GET /api/system/disk`

> `Return disk system information or a selected disk information category.`

---

## 🔹 Description

**Returns disk usage, partition, and I/O information collected by the disk service.**

The optional `category` query parameter limits the response to one disk information category.

---

## 🔹 Request

### Method

`GET`

### Path

`/api/system/disk`

### Authentication

`None`

### Path Parameters

| Parameter | Type | Required | Description                     |
| --------- | ---- | -------: | ------------------------------- |
| None      | —    |        — | No path parameters are defined. |

### Query Parameters

| Parameter  | Type     | Required | Default | Allowed Values              | Description                                   |
| ---------- | -------- | -------: | ------- | --------------------------- | --------------------------------------------- |
| `category` | `string` |       No | `None`  | `usage`, `partitions`, `io` | Selects a specific disk information category. |

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
get_disk_overview()
    │
    ▼
Select category if provided
    │
    ▼
JSON Response
```

1. Receive the request.
2. Validate the optional `category` parameter.
3. Collect disk information using `get_disk_overview()`.
4. Return the complete response or selected category.

---

## 🔹 Response

### Success

**Status:** `200 OK`

**Content-Type:** `application/json`

```json
{
    "usage": {},
    "partitions": [],
    "io": {}
}
```

### Response Fields

| Field        | Type     | Description                           |
| ------------ | -------- | ------------------------------------- |
| `usage`      | `object` | Disk usage information.               |
| `partitions` | `array`  | Available disk partition information. |
| `io`         | `object` | Disk I/O information.                 |

---

## 🔹 Metadata

No route-specific metadata is returned by the route itself.

API response metadata may be added by the global API middleware.

---

## 🔹 Status Codes

| Status | Meaning                                             |
| -----: | --------------------------------------------------- |
|  `200` | Disk information was returned successfully.         |
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
GET /api/system/disk
```

### Response

```json
{
    "usage": {},
    "partitions": [],
    "io": {}
}
```

### Request with Parameters

```http
GET /api/system/disk?category=usage
```

### Response

```json
{
    "usage": {}
}
```

---

## 🔹 Data Contract

```text
Disk
├── usage: object
├── partitions: array
└── io: object
```

---

## 🔹 Dependencies

* `FastAPI`
* `Query`
* `Literal`
* `get_disk_overview()`
* Disk system information services

---

## 🔹 Side Effects

* Reads disk usage information.
* Reads partition information.
* Reads disk I/O information.
* No persistent system state is modified.

---

## 🔹 Performance

Disk information is collected on each request. I/O and partition information may require system-level queries.

---

## 🔹 Security

* No authentication is required.
* The endpoint exposes local disk information.

---

## 🔹 Implementation

* **Module:** `jarbinlocalapi.api`
* **Route Function:** `get_api_system_disk`
* **Service:** `get_disk_overview()`
* **Router:** `api`

---

## 🔹 Route Contract

```text
METHOD      GET
PATH        /api/system/disk
AUTH        None
PARAMETERS  category
BODY        None
RESPONSE    JSON
SUCCESS     200
ERRORS      422
```

---

## 🔹 Notes

* `usage` is an object containing aggregate disk usage information.
* `partitions` is an array.
* `io` contains disk I/O information.

---
