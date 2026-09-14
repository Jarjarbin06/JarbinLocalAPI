# `GET /app/system`

> `Display an overview of the current system state.`

---

## 🔹 Description

**Displays a consolidated overview of CPU, memory, storage, network, process, system, battery, temperature, and top process information.**

---

## 🔹 Page

**Path:** `/app/system`

**Authentication:** `None`

**Content-Type:** `text/html`

---

## 🔹 Content

* CPU usage, logical CPU count, frequency, and load.
* Virtual memory and swap usage.
* Storage usage and capacity.
* Network interface status.
* Running process count and process ID count.
* System boot time and logged-in user count.
* Battery status and remaining time when a battery is available.
* Temperature sensor readings.
* Top five processes sorted by CPU usage.
* Links to detailed system information pages.
* Back button for returning to the previous page.

---

## 🔹 Dependencies

* `system.html`
* `/static/css/main.css`
* `/api/system`
* `/app/system/cpu`
* `/app/system/memory`
* `/app/system/disk`
* `/app/system/network`
* `/app/system/processes`
* `/app/system/system`
* `/app/system/battery`
* `/app/system/temperatures`
* `/app/system/top_processes`

---

## 🔹 Notes

* System data is initially rendered server-side from `system`.
* The page displays battery information only when a battery is detected.
* Temperature information is grouped by sensor name.
* The top five processes are sorted by CPU usage in descending order.
* Detailed system information is accessible through the corresponding overview cards.
