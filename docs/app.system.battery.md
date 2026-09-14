# `GET /app/system/battery`

> `Display battery information and status.`

---

## 🔹 Description

**Displays the information reported by the system battery sensor, or indicates when no battery is detected.**

---

## 🔹 Page

**Path:** `/app/system/battery`

**Authentication:** `None`

**Content-Type:** `text/html`

---

## 🔹 Content

* Battery information and sensor values.
* Dynamically generated battery fields.
* Fallback message when no battery is detected.
* Back button for returning to the previous page.

---

## 🔹 Dependencies

* `battery.html`
* `/static/js/system/battery.js`
* `/static/css/main.css`
* `/api/system/sensors?category=battery`

---

## 🔹 Notes

* Battery data is initially rendered server-side from `battery.battery`.
* Battery fields are generated dynamically from the returned API data.
* The JavaScript client updates the displayed battery information using the system sensors API.
