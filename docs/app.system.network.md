# `GET /app/system/network`

> `Display network interfaces, status, I/O statistics, and connections.`

---

## 🔹 Description

**Displays information about the system network interfaces, their status, network I/O statistics, and active network connections.**

---

## 🔹 Page

**Path:** `/app/system/network`

**Authentication:** `None`

**Content-Type:** `text/html`

---

## 🔹 Content

* Network interfaces and their assigned addresses.
* Interface operational status, speed, and MTU.
* Network I/O counters for each interface.
* Active network connections and their associated information.
* Back button for returning to the previous page.
* Displays fallback messages when no interfaces or connections are available.

---

## 🔹 Dependencies

* `network.html`
* `/static/js/system/network.js`
* `/static/css/main.css`
* `/api/system/network`

---

## 🔹 Notes

* Network data is initially rendered server-side from `network`.
* Interface addresses are grouped by network interface.
* Network I/O fields are generated dynamically from the returned counters.
* Connection fields are generated dynamically from the returned connection objects.
