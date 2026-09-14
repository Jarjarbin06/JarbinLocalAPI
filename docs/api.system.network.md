# `GET /api/system/network`

> `Return network system information or a selected network category.`

---

## 🔹 Description

**Returns network interface, interface status, I/O, and connection information.**

The optional `category` query parameter limits the response to one network information category.

---

## 🔹 Request

### Method

`GET`

### Path

`/api/system/network`

### Authentication

`None`

### Path Parameters

| Parameter | Type | Required | Description                     |
| --------- | ---- | -------: | ------------------------------- |
| None      | —    |        — | No path parameters are defined. |

### Query Parameters

| Parameter  | Type     | Required | Default | Allowed Values                                        | Description                                      |
| ---------- | -------- | -------: | ------- | ----------------------------------------------------- | ------------------------------------------------ |
| `category` | `string` |       No | `None`  | `interfaces`, `interface_status`, `io`, `connections` | Selects a specific network information category. |

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
get_network_overview()
    │
    ▼
Select category if provided
    │
    ▼
JSON Response
```

1. Receive the request.
2. Validate the optional `category` parameter.
3. Collect network information using `get_network_overview()`.
4. Return the complete response or selected category.

---

## 🔹 Response

### Success

**Status:** `200 OK`

**Content-Type:** `application/json`

```json
{
    "interfaces": {},
    "interface_status": {},
    "io": {},
    "connections": []
}
```

### Response Fields

| Field              | Type     | Description                            |
| ------------------ | -------- | -------------------------------------- |
| `interfaces`       | `object` | Network interface information.         |
| `interface_status` | `object` | Network interface status information.  |
| `io`               | `object` | Network I/O information.               |
| `connections`      | `array`  | Active network connection information. |

---

## 🔹 Metadata

No route-specific metadata is returned by the route itself.

API response metadata may be added by the global API middleware.

---

## 🔹 Status Codes

| Status | Meaning                                             |
| -----: | --------------------------------------------------- |
|  `200` | Network information was returned successfully.      |
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
GET /api/system/network
```

### Response

```json
{
    "interfaces": {},
    "interface_status": {},
    "io": {},
    "connections": []
}
```

### Request with Parameters

```http
GET /api/system/network?category=interfaces
```

### Response

```json
{
    "interfaces": {}
}
```

---

## 🔹 Data Contract

```text
Network
├── interfaces: object
├── interface_status: object
├── io: object
└── connections: array
```

---

## 🔹 Dependencies

* `FastAPI`
* `Query`
* `Literal`
* `get_network_overview()`
* Network system information services

---

## 🔹 Side Effects

* Reads network interface information.
* Reads network connection information.
* Reads network I/O information.
* No persistent network state is modified.

---

## 🔹 Performance

Network information is collected on each request. Connection enumeration may vary in cost depending on the number of active connections.

---

## 🔹 Security

* No authentication is required.
* The endpoint exposes local network information.
* Connection information may contain addresses and ports.

---

## 🔹 Implementation

* **Module:** `jarbinlocalapi.api`
* **Route Function:** `get_api_system_network`
* **Service:** `get_network_overview()`
* **Router:** `api`

---

## 🔹 Route Contract

```text
METHOD      GET
PATH        /api/system/network
AUTH        None
PARAMETERS  category
BODY        None
RESPONSE    JSON
SUCCESS     200
ERRORS      422
```

---

## 🔹 Notes

* `interfaces`, `interface_status`, `io`, and `connections` are the available categories.
* Network information represents the current system state.

---
