# `GET /app/system/processes`

> `Display running processes and process statistics.`

---

## 🔹 Description

**Displays the current process count, process IDs, and detailed information about running processes.**

---

## 🔹 Page

**Path:** `/app/system/processes`

**Authentication:** `None`

**Content-Type:** `text/html`

---

## 🔹 Content

* Total number of running processes.
* List of process IDs.
* Process names and PIDs.
* CPU usage for each process.
* Memory usage for each process.
* Process status.
* Back button for returning to the previous page.

---

## 🔹 Dependencies

* `processes.html`
* `/static/js/system/processes.js`
* `/static/css/main.css`
* `/api/system/processes`

---

## 🔹 Notes

* Process data is initially rendered server-side from `processes`.
* Process information is displayed for every process returned by the API.
* The JavaScript client updates the displayed process information using the system processes API.
