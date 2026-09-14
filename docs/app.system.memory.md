# `GET /app/system/memory`

> `Display virtual and swap memory usage.`

---

## 🔹 Description

**Displays virtual memory and swap memory usage, including utilization percentages and available memory statistics.**

---

## 🔹 Page

**Path:** `/app/system/memory`

**Authentication:** `None`

**Content-Type:** `text/html`

---

## 🔹 Content

* Virtual memory usage percentage.
* Virtual memory statistics.
* Swap memory usage percentage.
* Swap memory statistics.
* Visual usage bars for virtual and swap memory.
* Back button for returning to the previous page.

---

## 🔹 Dependencies

* `memory.html`
* `/static/js/system/memory.js`
* `/static/css/main.css`
* `/api/system/memory`

---

## 🔹 Notes

* Memory data is initially rendered server-side from `memory`.
* The `percent` field is displayed separately from the other memory statistics.
* Virtual and swap memory fields are generated dynamically from their respective API responses.
