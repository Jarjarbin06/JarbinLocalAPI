# `GET /app/system/top_processes`

> `Display the processes currently consuming the most CPU resources.`

---

## 🔹 Description

**Displays the top CPU-consuming processes detected by JarbinLocalAPI.**

---

## 🔹 Page

**Path:** `/app/system/top_processes`

**Authentication:** `None`

**Content-Type:** `text/html`

---

## 🔹 Content

* List of processes sorted by CPU usage in descending order.
* Maximum of 10 processes displayed.
* Process name and PID.
* CPU usage percentage.
* Memory usage percentage.
* Process status.
* Back button for returning to the previous page.
* Displays a fallback message when no processes are available.

---

## 🔹 Dependencies

* `top_processes.html`
* `/static/js/system/top_processes.js`
* `/static/css/main.css`
* `/api/system/processes?category=processes`

---

## 🔹 Notes

* Processes are initially rendered server-side from the `top_processes.processes` data.
* The list is sorted by `cpu_percent` in descending order.
* Only the first 10 processes are displayed.
* The JavaScript client updates the displayed process information using the system processes API.
