# `GET /api`

> `Return the base JarbinLocalAPI message.`

---

## 🔹 Description

**Returns the base response of the JarbinLocalAPI API.**

The route provides a simple API-level endpoint for verifying that the API router is reachable and responding.

---

## 🔹 Request

### Method

`GET`

### Path

`/api/`

### Authentication

`None`

### Path Parameters

| Parameter | Type | Required | Description                     |
| --------- | ---- | -------: | ------------------------------- |
| None      | —    |        — | No path parameters are defined. |

### Query Parameters

| Parameter | Type | Required | Default | Allowed Values | Description                      |
| --------- | ---- | -------: | ------- | -------------- | -------------------------------- |
| None      | —    |        — | —       | —              | No query parameters are defined. |

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
API Router
    │
    ▼
get_api()
    │
    ▼
JSON Response
```

1. Receive the `GET /api/` request.
2. Execute `get_api()`.
3. Return the static JSON response.

---

## 🔹 Response

### Success

**Status:** `200 OK`

**Content-Type:** `application/json`

```json
{
    "message": "Hello World!"
}
```

### Response Fields

| Field     | Type     | Description                       |
| --------- | -------- | --------------------------------- |
| `message` | `string` | Base message returned by the API. |

---

## 🔹 Metadata

No route-specific metadata is returned by the route itself.

API response metadata may be added by the global API middleware.

---

## 🔹 Status Codes

| Status | Meaning                                       |
| -----: | --------------------------------------------- |
|  `200` | The API base endpoint responded successfully. |

---

## 🔹 Errors

No explicit errors are defined by the route.

---

## 🔹 Examples

### Request

```http
GET /api/
```

### Response

```json
{
    "message": "Hello World!"
}
```

### Request with Parameters

Not applicable.

### Response

Not applicable.

---

## 🔹 Data Contract

```text
Root
└── message: string
```

---

## 🔹 Dependencies

* `FastAPI`
* `jarbinlocalapi.api`
* `get_api`

---

## 🔹 Side Effects

* None

---

## 🔹 Performance

The route returns a static response without external or system resource access.

---

## 🔹 Security

* No authentication is required.
* The endpoint exposes only a static API message.

---

## 🔹 Implementation

* **Module:** `jarbinlocalapi.api`
* **Route Function:** `get_api`
* **Service:** None
* **Router:** `api`

---

## 🔹 Route Contract

```text
METHOD      GET
PATH        /api/
AUTH        None
PARAMETERS  None
BODY        None
RESPONSE    JSON
SUCCESS     200
ERRORS      None
```

---

## 🔹 Notes

* The endpoint is the base route of the API router.
* The returned message is static.
