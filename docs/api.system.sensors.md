# `GET /api/system/sensors`

> `Return sensor information or a selected sensor category.`

---

## 🔹 Description

**Returns temperature, fan, and battery sensor information collected from the system.**

The optional `category` query parameter limits the response to one sensor category.

---

## 🔹 Request

### Method

`GET`

### Path

`/api/system/sensors`

### Authentication

`None`

### Path Parameters

| Parameter | Type | Required | Description                     |
| --------- | ---- | -------: | ------------------------------- |
| None      | —    |        — | No path parameters are defined. |

### Query Parameters

| Parameter  | Type     | Required | Default | Allowed Values                    | Description                         |
| ---------- | -------- | -------: | ------- | --------------------------------- | ----------------------------------- |
| `category` | `string` |       No | `None`  | `temperatures`, `fans`, `battery` | Selects a specific sensor category. |

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
get_sensors_overview()
    │
    ▼
Select category if provided
    │
    ▼
JSON Response
```

1. Receive the request.
2. Validate the optional `category` parameter.
3. Collect sensor information using `get_sensors_overview()`.
4. Return the complete response or selected category.

---

## 🔹 Response

### Success

**Status:** `200 OK`

**Content-Type:** `application/json`

```json
{
    "temperatures": {},
    "fans": {},
    "battery": {}
}
```

### Response Fields

| Field          | Type              | Description                                              |
| -------------- | ----------------- | -------------------------------------------------------- |
| `temperatures` | `object`          | Temperature sensor information grouped by sensor source. |
| `fans`         | `object`          | Fan sensor information grouped by sensor source.         |
| `battery`      | `object` / `null` | Battery information when a battery is detected.          |

---

## 🔹 Metadata

No route-specific metadata is returned by the route itself.

API response metadata may be added by the global API middleware.

---

## 🔹 Status Codes

| Status | Meaning                                             |
| -----: | --------------------------------------------------- |
|  `200` | Sensor information was returned successfully.       |
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
GET /api/system/sensors
```

### Response

```json
{
    "temperatures": {},
    "fans": {},
    "battery": {}
}
```

### Request with Parameters

```http
GET /api/system/sensors?category=temperatures
```

### Response

```json
{
    "temperatures": {}
}
```

---

## 🔹 Data Contract

```text
Sensors
├── temperatures: object
├── fans: object
└── battery: object | null
```

---

## 🔹 Dependencies

* `FastAPI`
* `Query`
* `Literal`
* `get_sensors_overview()`
* System sensor services

---

## 🔹 Side Effects

* Reads temperature sensor information.
* Reads fan information.
* Reads battery information.
* No sensor state is modified.

---

## 🔹 Performance

Sensor information is collected on each request. Availability and collection cost depend on the sensors exposed by the host system.

---

## 🔹 Security

* No authentication is required.
* The endpoint exposes local hardware sensor information.

---

## 🔹 Implementation

* **Module:** `jarbinlocalapi.api`
* **Route Function:** `get_api_system_sensors`
* **Service:** `get_sensors_overview()`
* **Router:** `api`

---

## 🔹 Route Contract

```text
METHOD      GET
PATH        /api/system/sensors
AUTH        None
PARAMETERS  category
BODY        None
RESPONSE    JSON
SUCCESS     200
ERRORS      422
```

---

## 🔹 Notes

* `battery` may be `null` when no battery is detected.
* `temperatures` and `fans` depend on available hardware sensors.
* The route does not expose separate routes for these categories.

---
