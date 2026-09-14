# `GET /app/system/temperatures`

> `Display temperatures reported by available system sensors.`

---

## 🔹 Description

**Displays the current temperatures reported by the system's available temperature sensors.**

---

## 🔹 Page

**Path:** `/app/system/temperatures`

**Authentication:** `None`

**Content-Type:** `text/html`

---

## 🔹 Content

* Temperature sensors grouped by sensor name.
* Temperature sensor labels.
* Current temperature values in degrees Celsius.
* Back button for returning to the previous page.
* Displays a fallback message when no temperature sensors are available.

---

## 🔹 Dependencies

* `temperatures.html`
* `/static/js/system/temperatures.js`
* `/static/css/main.css`
* `/api/system/sensors?category=temperatures`

---

## 🔹 Notes

* Temperature data is initially rendered server-side from `temperatures.temperatures`.
* Each sensor group can contain multiple temperature entries.
* The JavaScript client updates the displayed temperatures using the system sensors API.
