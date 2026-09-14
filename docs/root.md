# `GET /`

> Get the current JarbinLocalAPI server status.

---

## 🔹 Description

**Returns the current operational status of the JarbinLocalAPI server.**

---

## 🔹 Request

### Method

`GET`

### Path

`/`

### Authentication

`None`

### Path Parameters

None.

### Query Parameters

None.

### Headers

None.

### Body

None.

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
Root route
    │
    ▼
Generate server status
    │
    ▼
JSON response
```

1. Receive the `GET /` request.
2. Execute the root route.
3. Return the server status.

---

## 🔹 Response

### Success

**Status:** `200 OK`

**Content-Type:** `application/json`

```json
{
    "status": "OK"
}
```

### Response Fields

| Field    | Type     | Description            |
| -------- | -------- | ---------------------- |
| `status` | `string` | Current server status. |

---

## 🔹 Metadata

None.

---

## 🔹 Status Codes

| Status | Meaning                              |
| -----: | ------------------------------------ |
|  `200` | Server status returned successfully. |

---

## 🔹 Errors

None explicitly defined by the route.

---

## 🔹 Examples

### Request

```http
GET /
```

### Response

```json
{
    "status": "OK"
}
```

### Request with Parameters

None.

### Response

None.

---

## 🔹 Data Contract

```text
Root
└── status: string
```

---

## 🔹 Dependencies

* `jarbinlocalapi`

---

## 🔹 Side Effects

None.

---

## 🔹 Performance

Returns a static status value without performing system or external resource queries.

---

## 🔹 Security

* No authentication is required.
* The route exposes only the server operational status.

---

## 🔹 Implementation

* **Module:** `jarbinlocalapi.main`
* **Route Function:** `get_root`
* **Service:** None.
* **Router:** `jarbinlocalapi`

---

## 🔹 Route Contract

```text
METHOD      GET
PATH        /
AUTH        None
PARAMETERS  None
BODY        None
RESPONSE    JSON
SUCCESS     200
ERRORS      None
```

---

## 🔹 Notes

* The route is available at the root of the FastAPI application.
* The current implementation always returns `"OK"` when the route executes successfully.
