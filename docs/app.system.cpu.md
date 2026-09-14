# `GET /app/system/cpu`

> `Display CPU usage, frequency, load, and statistics.`

---

## 🔹 Description

**Displays detailed CPU information including utilization, processor count, frequency, load averages, CPU times, and CPU statistics.**

---

## 🔹 Page

**Path:** `/app/system/cpu`

**Authentication:** `None`

**Content-Type:** `text/html`

---

## 🔹 Content

* Current CPU usage percentage with a visual usage bar.
* Number of logical CPUs.
* Current, minimum, and maximum CPU frequency.
* 1, 5, and 15 minute load averages.
* CPU time statistics.
* CPU time percentages.
* CPU statistics.
* Back button for returning to the previous page.

---

## 🔹 Dependencies

* `cpu.html`
* `/static/js/system/cpu.js`
* `/static/css/main.css`
* `/api/system/cpu`

---

## 🔹 Notes

* CPU data is initially rendered server-side from `cpu`.
* CPU time, percentage, and statistics fields are generated dynamically from the returned API data.
* The JavaScript client updates the displayed CPU information using the system CPU API.
