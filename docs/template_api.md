# `<METHOD> <PATH>`

> `<Short technical description of the route>`

---

## 🔹 Description

**<Detailed description of what the route does.>**

---

## 🔹 Request

### Method

`<METHOD>`

### Path

`<PATH>`

### Authentication

`<None / Required / ...>`

### Path Parameters

| Parameter | Type     |   Required | Description     |
| --------- | -------- | ---------: | --------------- |
| `<name>`  | `<type>` | `<Yes/No>` | `<description>` |

### Query Parameters

| Parameter | Type     |   Required | Default     | Allowed Values | Description     |
| --------- | -------- | ---------: | ----------- | -------------- | --------------- |
| `<name>`  | `<type>` | `<Yes/No>` | `<default>` | `<values>`     | `<description>` |

### Headers

| Header     |   Required | Description     |
| ---------- | ---------: | --------------- |
| `<header>` | `<Yes/No>` | `<description>` |

### Body

```json
{
    "<field>": "<value>"
}
```

| Field     | Type     |   Required | Description     |
| --------- | -------- | ---------: | --------------- |
| `<field>` | `<type>` | `<Yes/No>` | `<description>` |

---

## 🔹 Settings

| Setting        | Value                 |
| -------------- | --------------------- |
| Response Type  | `<JSON / HTML / ...>` |
| Authentication | `<None / ...>`        |
| Cacheable      | `<Yes / No>`          |
| Streaming      | `<Yes / No>`          |
| Idempotent     | `<Yes / No>`          |

---

## 🔹 Processing

```text
Request
    │
    ▼
<Validation>
    │
    ▼
<Processing / Service>
    │
    ▼
<Response generation>
    │
    ▼
Response
```

1. `<Step>`
2. `<Step>`
3. `<Step>`

---

## 🔹 Response

### Success

**Status:** `<STATUS> <STATUS NAME>`

**Content-Type:** `<application/json>`

```json
{
    "data": {},
    "meta": {}
}
```

### Response Fields

| Field     | Type     | Description     |
| --------- | -------- | --------------- |
| `<field>` | `<type>` | `<description>` |

---

## 🔹 Metadata

| Field     | Type     | Description     |
| --------- | -------- | --------------- |
| `<field>` | `<type>` | `<description>` |

---

## 🔹 Status Codes

|  Status | Meaning         |
| ------: | --------------- |
| `<200>` | `<description>` |
| `<400>` | `<description>` |
| `<404>` | `<description>` |
| `<500>` | `<description>` |

---

## 🔹 Errors

### `<STATUS> <STATUS NAME>`

```json
{
    "detail": "<error message>"
}
```

**Cause:** `<description>`

---

## 🔹 Examples

### Request

```http
<METHOD> <PATH>
```

### Response

```json
{
    "data": {},
    "meta": {}
}
```

### Request with Parameters

```http
<METHOD> <PATH>?<parameter>=<value>
```

### Response

```json
{
    "data": {},
    "meta": {}
}
```

---

## 🔹 Data Contract

```text
<Root>
├── <field>: <type>
├── <field>: <type>
└── <field>: <type>
    ├── <field>: <type>
    └── <field>: <type>
```

---

## 🔹 Dependencies

* `<Python module>`
* `<JarbinLocalAPI service>`
* `<System resource>`
* `<External dependency>`

---

## 🔹 Side Effects

* `<Effect>`
* `<Effect>`

---

## 🔹 Performance

`<Performance characteristics or relevant constraints.>`

---

## 🔹 Security

* `<Security property>`
* `<Security limitation>`

---

## 🔹 Implementation

* **Module:** `<module>`
* **Route Function:** `<function>`
* **Service:** `<service>`
* **Router:** `<router>`

---

## 🔹 Route Contract

```text
METHOD      <METHOD>
PATH        <PATH>
AUTH        <value>
PARAMETERS  <value>
BODY        <value>
RESPONSE    <value>
SUCCESS     <status>
ERRORS      <status codes>
```

---

## 🔹 Notes

* `<Technical note>`
* `<Technical note>`
